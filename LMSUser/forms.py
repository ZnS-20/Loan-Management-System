from django import forms
from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','middle_name','last_name','email','phone','password1','password2')
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "middle_name": "Middle Name",
            "email": "Email",
            "phone": "Phone",
            "password1": "Password",
            "password2": "Confirm Password",
        }
        widgets = {
            "first_name": forms.TextInput(attrs = {"class":"form-control"}),
            "middle_name": forms.TextInput(attrs = {"class":"form-control"}),
            "last_name": forms.TextInput(attrs = {"class":"form-control"}),
            "email": forms.EmailInput(attrs = {"class":"form-control"}),
            "phone": forms.TextInput(attrs = {"class":"form-control"}),
            "password1": forms.PasswordInput(attrs = {"class":"form-control"}),
            "password2": forms.PasswordInput(attrs = {"class":"form-control"}),
        }