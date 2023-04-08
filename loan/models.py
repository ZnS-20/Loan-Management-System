from django.db import models
from LMSUser.models import CustomUser
from django.utils import timezone
# Create your models here.


class LoanTypes(models.Model):
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    version_number = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.type


class SalaryTypes(models.Model):
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    version_number = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.type


class BasicDetails(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    address1 = models.CharField(max_length=512)
    zipcode1 = models.CharField(max_length=6)
    address2 = models.CharField(max_length=512)
    zipcode2 = models.CharField(max_length=6)
    salary_type = models.OneToOneField(
        SalaryTypes, on_delete=models.SET_NULL, null=True)
    loan_type = models.OneToOneField(
        LoanTypes, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    version_number = models.IntegerField(default=0)
