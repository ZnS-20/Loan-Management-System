from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.
def home(request):
    return render(request,'LMSUser/home.html',{})

def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('register_user')
    else:
        form = UserForm
        return render(request,'LMSUser/register_user.html',{"form":form})