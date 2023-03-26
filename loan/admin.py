from django.contrib import admin
from .models import LoanTypes, BasicDetails
# Register your models here.
admin.site.register(LoanTypes)
admin.site.register(BasicDetails)
