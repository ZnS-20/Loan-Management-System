from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserDetails
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'LMSUser/home.html', {})


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
            return redirect('home')
        else:
            return render(request, 'LMSUser/register_user.html', {"form": form, "formDetails": formDetails})
    else:
        form = UserRegisterForm
        formDetails = UserDetails
        return render(request, 'LMSUser/register_user.html', {"form": form, "formDetails": formDetails})
