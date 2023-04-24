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
    salary_type = models.ForeignKey(
        SalaryTypes, on_delete=models.SET_NULL, null=True)
    loan_type = models.ForeignKey(
        LoanTypes, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=256)
    modified_at = models.DateTimeField(default=timezone.now)
    modified_by = models.CharField(max_length=256)
    amount = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=7, default=0)
    version_number = models.IntegerField(default=0)


class documents(models.Model):
    file = models.BinaryField(null=False)
    file_format = models.CharField(
        max_length=6, help_text="Stores the type of document i.e, pdf, jpeg, jpg, etc.")
    document_name = models.CharField(
        max_length=60, help_text="Store the name of the file.")
    document_type = models.CharField(
        max_length=60, help_text="Store the type of document uploaded. ex: Address Proof, income proof")
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=256)
    modified_at = models.DateTimeField(default=timezone.now)
    modified_by = models.CharField(max_length=256)
    version_number = models.IntegerField(default=0)
