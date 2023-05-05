from django.shortcuts import render, redirect
from django.contrib import messages
from LMSUser.models import CustomUser
from .models import documents, BasicDetails
from .functions import deleteDocuments, getFormType, getListofDocuments, getFormObject, calculateEMI, setInitialUserDetails, setBasicDetails
from .forms import LoanForm
import datetime


def viewAllLoan(request):
    """Functions returns a list of loans
    get:
    Return a page showing list of loans in a bootstrap table.
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Please login to view you loans.')
        return redirect('home')
    user = CustomUser.objects.get(user=request.user.id)
    loans = BasicDetails.objects.filter(user=user)
    print(type(loans))
    return render(request, 'loan/viewApplications.html', {'loans': loans})


def editDetails(request, basicdetails_id):
    """Functions is used to update basic details for the perticular id(basicdetails_id)
    get:
    return the form with initial values stored in database.

    post:
    updates the database table BasicDetails with id = basicdetails_id
    """
    basicDetail = BasicDetails.objects.get(pk=basicdetails_id)
    loan_type = basicDetail.loan_type
    salary_type = basicDetail.salary_type
    if (not request.user.is_authenticated) or basicDetail.user.user != request.user:
        messages.error(request, "Denied! Unauthorized Access.")
        return redirect('home')

    if basicDetail.submitted:
        messages.error(request, "Application Already Submitted!")
        return render(request, 'LMSUser/home.html', {})

    user = CustomUser.objects.get(user=request.user.id)
    if request.method == "POST":
        form = LoanForm(request.POST, instance=basicDetail)
        if form.is_valid():
            basicdetails = form.save(commit=False)
            basicdetails.user = user
            basicdetails.created_by = user.user.first_name+' '+user.user.last_name
            basicdetails.modified_by = user.user.first_name+' '+user.user.last_name
            basicdetails.modified_at = datetime.datetime.now()
            basicdetails.save()

            if loan_type != form.cleaned_data['loan_type'] or salary_type != form.cleaned_data['salary_type']:
                deleteDocuments(basicDetail)
                return redirect('uploadDocument', basicdetails_id=basicdetails.pk)

            return redirect('reviewApplication', basicdetails_id=basicdetails_id)
    else:
        userDict = setInitialUserDetails(user)
        initial = setBasicDetails(basicDetail, userDict)
        form = LoanForm(initial=initial)
        return render(request, 'loan/editDetails.html', {'form': form})


def submitApplication(request, basicdetails_id):
    """
    The function is used to update the submitted column in Basic Details Table to true.
    """
    basicDetail = BasicDetails.objects.get(pk=basicdetails_id)
    if (not request.user.is_authenticated) or request.user != basicDetail.user.user:
        messages.error(request, "Denied! Unauthorized Access.")
        return render(request, 'LMSUser/home.html', {})

    if basicDetail.submitted:
        messages.error(request, "Application Already Submitted!")
        return render(request, 'LMSUser/home.html', {})

    basicDetail.submitted = True
    basicDetail.save()
    messages.success(request, "Loan Submitted Successfully.")
    return redirect('home')


def reviewApplication(request, basicdetails_id):
    """
    The Function returns the list of uploaded documents, details of loan as saved by the user and the calulated EMIs.
    """
    basicDetail = BasicDetails.objects.get(pk=basicdetails_id)
    if (not request.user.is_authenticated) or request.user != basicDetail.user.user:
        messages.error(request, "Denied! Unauthorized Access.")
        return render(request, 'LMSUser/home.html', {})

    if basicDetail.submitted:
        messages.error(request, "Application Already Submitted!")
        return render(request, 'LMSUser/home.html', {})

    if documents.objects.filter(loan_id=basicDetail).count() < 6:
        messages.error(request, "Please upload all the required documents")
        return redirect('uploadDocument', basicdetails_id=basicdetails_id)

    documentList = documents.objects.filter(loan_id=basicdetails_id)
    emi = calculateEMI(basicDetail.amount, basicDetail.loan_type.interest_rate,
                       basicDetail.tenure, basicDetail.loan_type.down_payment)
    interestAmount = basicDetail.amount - emi*basicDetail.tenure
    totalAmountPayable = emi*basicDetail.tenure
    if (basicDetail.loan_type.down_payment > 0):
        downpayment = (basicDetail.loan_type.down_payment/100) * \
            basicDetail.amount
        totalAmountPayable += downpayment
        interestAmount -= downpayment
    else:
        downpayment = 0
    interestAmount = interestAmount*- \
        1 if (interestAmount < 0) else interestAmount
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
    if (not request.user.is_authenticated) or request.user != basicDetail.user.user:
        messages.error(request, "Denied! Unauthorized Access.")
        return render(request, 'LMSUser/home.html', {})

    if basicDetail.submitted:
        messages.error(request, "Application Already Submitted!")
        return render(request, 'LMSUser/home.html', {})

    formType = getFormType(basicDetail)
    form = getFormObject(formType, request)
    if request.method == "POST":
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


def applyLoan(request):
    """The Function is used to store the basic details of the user in db.
    get:
    Returns Form containing basic details field

    post:
    Insert data into db.
    """
    if not request.user.is_authenticated:
        messages.error(request, "Denied! Unauthorized Access.")
        return render(request, 'LMSUser/home.html', {})

    current_user = request.user.id
    user = CustomUser.objects.get(user=current_user)
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            basicdetails = form.save(commit=False)
            basicdetails.user = user
            basicdetails.created_by = user.user.first_name+' '+user.user.last_name
            basicdetails.modified_by = user.user.first_name+' '+user.user.last_name
            basicdetails.save()
            return redirect('uploadDocument', basicdetails_id=basicdetails.pk)
        else:
            messages.error(request, "Invalid Fields! Try Again")
            form = LoanForm(initial=initial)
            return render(request, 'loan/applyloan.html', {'form': form})
    else:
        initial = setInitialUserDetails(user)
        form = LoanForm(initial=initial)
        return render(request, 'loan/applyloan.html', {'form': form})
