from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserDetails
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, 'LMSUser/home.html', {})


def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'LMSUser/Login.html', {})


def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        formDetails = UserDetails(request.POST)
        if form.is_valid() and formDetails.is_valid():
            user = form.save()
            user.refresh_from_db()
            userdetails = formDetails.save(commit=False)
            userdetails.user = user
            userdetails.save()
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'LMSUser/register_user.html', {"form": form, "formDetails": formDetails})
    else:
        form = UserRegisterForm
        formDetails = UserDetails
        return render(request, 'LMSUser/register_user.html', {"form": form, "formDetails": formDetails})
