from django.shortcuts import render, redirect
from django.contrib import messages
from LMSUser.models import CustomUser
from .models import documents, BasicDetails
from .functions import getFormType, getListofDocuments, getFormObject, calculateEMI, setInitialUserDetails, setBasicDetails
from .forms import LoanForm
import datetime


def submitApplication(request, basicdetails_id):
    """
    The function is used to update the submitted column in Basic Details Table to true.
    """
    basicDetail = BasicDetails.objects.get(pk=basicdetails_id)
    if not request.user.is_authenticated:
        return redirect('applyLoan')
    basicDetail.submitted = True
    basicDetail.save()
    return redirect('home')


def reviewApplication(request, basicdetails_id):
    """
    The Function returns the list of uploaded documents, details of loan as saved by the user and the calulated EMIs.
    """
    basicDetail = BasicDetails.objects.get(pk=basicdetails_id)
    if not request.user.is_authenticated and request.user == basicDetail.user.user:
        return render(request, 'LMSUser/home.html', {})
    documentList = documents.objects.filter(loan_id=basicdetails_id)
    emi = calculateEMI(basicDetail.amount, basicDetail.loan_type.interest_rate,
                       basicDetail.tenure, basicDetail.loan_type.down_payment)
    totalAmountPayable = emi*basicDetail.tenure
    interestAmount = totalAmountPayable - basicDetail.amount
    if (basicDetail.loan_type.down_payment > 0):
        downpayment = (basicDetail.loan_type.down_payment/100) * \
            basicDetail.amount
    else:
        downpayment = None
    return render(request, 'loan/reviewApplication.html',
                  {'basicDetails': basicDetail, 'documentList': documentList, 'emi': int(emi),
                   'totalAmountPayable': int(totalAmountPayable), 'interestAmount': int(interestAmount),
                   'downpayment': int(downpayment)})


def uploadDocument(request, basicdetails_id):
    """
    The Function is used to upload a list of documents required for loan

    get:
    Return a form containing the list of document

    post:
    Upload documents and save in database. 
    """
    basicDetail = BasicDetails.objects.get(pk=basicdetails_id)
    if not request.user.is_authenticated and request.user == basicDetail.user.user:
        return render(request, 'LMSUser/home.html', {})
    formType = getFormType(basicDetail)
    form = getFormObject(formType, request)
    if request.method == "POST":
        print(formType)
        # each type of loan contains different types of documents.
        docList = getListofDocuments(formType)
        if form.is_valid():
            for doc_type in docList:
                uploadFile = request.FILES[doc_type]
                extension = uploadFile.name.split('.', 1)[-1]
                doc = documents(file=uploadFile, file_format=extension, document_name=uploadFile.name, document_type=doc_type,
                                loan_id=basicDetail, created_by=request.user, modified_by=request.user)
                doc.save()
            return redirect('reviewApplication', basicdetails_id=basicdetails_id)
        else:
            return render(request, 'loan/uploadDocument.html',
                          {'form': form})
    else:
        return render(request, 'loan/uploadDocument.html',
                      {'form': form})


def applyLoan(request, basicdetails_id):
    if not request.user.is_authenticated:
        return render(request, 'LMSUser/home.html', {})
    current_user = request.user.id
    user = CustomUser.objects.get(user=current_user)
    if request.method == "POST":
        if int(basicdetails_id) > 0:
            instance = BasicDetails.objects.get(pk=basicdetails_id)
            form = LoanForm(request.POST, instance=instance)
        else:
            form = LoanForm(request.POST)
        if form.is_valid():
            if int(basicdetails_id) > 0:
                basicdetails = form.save(commit=False)
                basicdetails.user = user
                basicdetails.created_by = user.user.first_name+' '+user.user.last_name
                basicdetails.modified_by = user.user.first_name+' '+user.user.last_name
                basicdetails.modified_at = datetime.datetime.now()
                basicdetails.save()
                return redirect('reviewApplication', basicdetails_id=basicdetails_id)
            else:
                basicdetails = form.save(commit=False)
                basicdetails.user = user
                basicdetails.created_by = user.user.first_name+' '+user.user.last_name
                basicdetails.modified_by = user.user.first_name+' '+user.user.last_name
                basicdetails.save()
                return redirect('uploadDocument', basicdetails_id=basicdetails.pk)
        else:
            messages.error(request, "Invalid Fields! Try Again")
            form = LoanForm(initial=initial)
            return render(request, 'loan/applyloan.html', {'form': form, 'basicdetails_id': int(basicdetails_id)})
    else:
        initial = setInitialUserDetails(user)
        form = LoanForm(request.POST or None, initial=initial)
        if int(basicdetails_id) > 0:
            basicdetail = BasicDetails.objects.get(pk=basicdetails_id)
            initial = setBasicDetails(basicdetail, initial)
            form = LoanForm(initial=initial)
            return render(request, 'loan/applyloan.html', {'form': form, 'basicdetails_id': int(basicdetails_id)})
        else:
            return render(request, 'loan/applyloan.html', {'form': form, 'basicdetails_id': basicdetails_id})
