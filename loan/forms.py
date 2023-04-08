from django import forms
from django.forms import ModelForm
from .models import BasicDetails
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
        fields = ("first_name", "middle_name", "last_name", "email", "phone", "address1", "zipcode1", "address2",
                  "zipcode2", "salary_type", "loan_type")
        widgets = {
            "address1": forms.Textarea(attrs={'class': 'form-control'}),
            "zipcode1": forms.TextInput(attrs={'class': 'form-control'}),
            "address2": forms.Textarea(attrs={'class': 'form-control'}),
            "zipcode2": forms.TextInput(attrs={'class': 'form-control'}),
            "salary_type": forms.Select(attrs={'class': 'form-control'}),
            "loan_type": forms.Select(attrs={'class': 'form-control'}),
        }
