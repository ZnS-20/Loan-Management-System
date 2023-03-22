from django import forms
from django.forms import ModelForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserDetails(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('middle_name', 'phone')
        widgets = {
            "middle_name": forms.TextInput(attrs={'class': 'form-control'}),
            "phone": forms.TextInput(attrs={'class': 'form-control'})
        }


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'last_name'}))
    password1 = forms.CharField(
        widget=(forms.PasswordInput(attrs={'class': 'form-control'})))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
