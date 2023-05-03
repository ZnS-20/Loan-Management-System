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
                  "salary_type", "loan_type", "amount", "tenure")
        widgets = {
            "address1": forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 5em'}),
            "zipcode1": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            "address2": forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 5em'}),
            "zipcode2": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            "salary_type": forms.Select(attrs={'class': 'form-control'}),
            "loan_type": forms.Select(attrs={'class': 'form-control'}),
            "amount": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            "tenure": forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }


class PersonalSalariedForm(forms.Form):
    address_proof = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    identity_proof = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    passport_photo = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}))
    salaryslip1 = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    salaryslip2 = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    salaryslip3 = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))


class PersonalBusinessForm(forms.Form):
    address_proof = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    identity_proof = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    passport_photo = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}))
    itr_y1 = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    itr_y2 = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    itr_y3 = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))


class EducationSalaried(forms.Form):
    address_proof = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    identity_proof = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    passport_photo = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}))
    high_school_marksheet = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    recommendation_letter = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    proof_of_income = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))


class HomeSalaried(forms.Form):
    address_proof = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    identity_proof = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    passport_photo = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}))
    salaryslip_m1 = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    salaryslip_m2 = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    salaryslip_m3 = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    property_doc = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))


class HomeBusiness(forms.Form):
    address_proof = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    identity_proof = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    passport_photo = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}))
    itr_y1 = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    itr_y2 = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    itr_y3 = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
    property_doc = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/jpeg,image/gif,image/png,application/pdf'}))
