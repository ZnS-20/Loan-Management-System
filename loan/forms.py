from django import forms
from django.forms import ModelForm
from .models import BasicDetails, documents
from LMSUser.models import CustomUser


class LoanForm(ModelForm):
    first_name = forms.CharField(max_length=50, disabled=True, widget=forms.TextInput(
        attrs={'class': 'form-control', }), required=False)
    middle_name = forms.CharField(max_length=50, disabled=True, widget=forms.TextInput(
        attrs={'class': 'form-control', }), required=False)
    last_name = forms.CharField(max_length=50, disabled=True, widget=forms.TextInput(
        attrs={'class': 'form-control', }), required=False)
    email = forms.CharField(max_length=256, disabled=True, widget=forms.TextInput(
        attrs={'class': 'form-control', }), required=False)
    phone = forms.CharField(max_length=10, disabled=True, widget=forms.TextInput(
        attrs={'class': 'form-control', }), required=False)

    class Meta:
        model = BasicDetails
        fields = ("first_name", "middle_name", "last_name", "email", "phone", "address1", "address2",
                  "salary_type", "loan_type", "amount")
        widgets = {
            "address1": forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 5em'}),
            "zipcode1": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            "address2": forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 5em'}),
            "zipcode2": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            "salary_type": forms.Select(attrs={'class': 'form-control'}),
            "loan_type": forms.Select(attrs={'class': 'form-control'}),
            "amount": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }


class DocumentUploadForm(ModelForm):
    class Meta:
        model = documents
        fields = ("file", "file_format", "document_name", "document_type",
                  "created_at", "created_by", "modified_at", "modified_by", "version_number")


class PersonalSalariedForm(forms.Form):
    address_proof = forms.FileField()
    identity_proof = forms.FileField()
    passport_photo = forms.FileField()
    salaryslip1 = forms.FileField()
    salaryslip2 = forms.FileField()
    salaryslip3 = forms.FileField()


class PersonalBusinessForm(forms.Form):
    address_proof = forms.FileField()
    identity_proof = forms.FileField()
    passport_photo = forms.FileField()
    itr_y1 = forms.FileField()
    itr_y2 = forms.FileField()
    itr_y3 = forms.FileField()


class EducationSalaried(forms.Form):
    address_proof = forms.FileField()
    identity_proof = forms.FileField()
    passport_photo = forms.FileField()
    high_school_marksheet = forms.FileField()
    recommendation_letter = forms.FileField()
    proof_of_income = forms.FileField()


class HomeSalaried(forms.Form):
    address_proof = forms.FileField()
    identity_proof = forms.FileField()
    passport_photo = forms.FileField()
    salaryslip_m1 = forms.FileField()
    salaryslip_m2 = forms.FileField()
    salaryslip_m3 = forms.FileField()
    property_doc = forms.FileField()


class HomeBusiness(forms.Form):
    address_proof = forms.FileField()
    identity_proof = forms.FileField()
    passport_photo = forms.FileField()
    itr_y1 = forms.FileField()
    itr_y2 = forms.FileField()
    itr_y3 = forms.FileField()
    property_doc = forms.FileField()
