from django.shortcuts import render, redirect
from django.contrib import messages
from LMSUser.models import CustomUser

# Create your views here.
from .forms import LoanForm


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
                return redirect('home')
            else:
                messages.error(request, "Invalid Fields! Try Again")
                return render(request, 'loan/applyloan.html', {'form': form})
        else:
            return render(request, 'loan/applyloan.html', {'form': form})
