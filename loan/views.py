from django.shortcuts import render, redirect
from django.contrib import messages
from LMSUser.models import CustomUser
from .models import documents, BasicDetails
from .functions import getFormType, getListofDocuments, getFormObject
from .forms import LoanForm


def reviewApplication(request, basicdetails_id):
    basicDetails = BasicDetails.objects.get(pk=basicdetails_id)
    documentList = documents.objects.filter(loan_id=basicdetails_id)
    print(basicDetails.amount)
    return render(request, 'loan/reviewApplication.html', {'basicDetails': basicDetails, 'documentList': documentList})


def uploadDocument(request, basicdetails_id):
    if not request.user.is_authenticated:
        return render(request, 'LMSUser/home.html', {})
    basicDetails = BasicDetails.objects.get(pk=basicdetails_id)
    formType = getFormType(basicDetails)
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
                                loan_id=basicDetails, created_by=request.user, modified_by=request.user)
                doc.save()
            return redirect('reviewApplication', basicdetails_id=basicdetails_id)
        else:
            return render(request, 'loan/uploadDocument.html',
                          {'form': form})
    else:
        return render(request, 'loan/uploadDocument.html',
                      {'form': form})


def applyLoan(request):
    if not request.user.is_authenticated:
        return render(request, 'LMSUser/home.html', {})
    else:
        current_user = request.user.id
        user = CustomUser.objects.get(user=current_user)
        initial = {
            "first_name": user.user.first_name,
            "middle_name": user.middle_name,
            "last_name": user.user.last_name,
            "email": user.user.email,
            "phone": user.phone,
            "user": user
        }
        form = LoanForm(request.POST or None, initial=initial)
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
            return render(request, 'loan/applyloan.html', {'form': form})
