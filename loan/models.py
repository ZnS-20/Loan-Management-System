from django.db import models
from LMSUser.models import CustomUser
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class LoanTypes(models.Model):
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    version_number = models.IntegerField(default=0)
    interest_rate = models.DecimalField(
        decimal_places=2, max_digits=4, default=7.2, validators=[MinValueValidator(7.1), MaxValueValidator(15.0)])
    down_payment = models.DecimalField(
        default=0.0, max_digits=20, decimal_places=4, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.type


class SalaryTypes(models.Model):
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    version_number = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.type


class BasicDetails(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    address1 = models.CharField(
        "Address1 will store the Current Address", max_length=512)
    address2 = models.CharField(
        "Address1 will store the Permanent Address", max_length=512)
    salary_type = models.ForeignKey(
        SalaryTypes, on_delete=models.SET_NULL, null=True)
    loan_type = models.ForeignKey(
        LoanTypes, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=256)
    modified_at = models.DateTimeField(default=timezone.now)
    modified_by = models.CharField(max_length=256)
    submitted = models.BooleanField(null=False, blank=False, default=False)
    amount = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=20, default=0.0, validators=[MinValueValidator(0.01)])
    tenure = models.IntegerField(
        null=False, blank=False, default=12, help_text="Minimum Tenure should be 12 months and Maximum Tensure will be 360 months", validators=[
            MaxValueValidator(360),
            MinValueValidator(1)
        ])
    version_number = models.IntegerField(default=0)


class documents(models.Model):
    class Meta:
        unique_together = (('document_type', 'loan_id'),)
    file = models.FileField()
    file_format = models.CharField(
        max_length=6, help_text="Stores the type of document i.e, pdf, jpeg, jpg, etc.")
    document_name = models.CharField(
        max_length=60, help_text="Store the name of the file.")
    document_type = models.CharField(
        max_length=60, help_text="Store the type of document uploaded. ex: Address Proof, income proof")
    loan_id = models.ForeignKey(
        BasicDetails, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=256)
    modified_at = models.DateTimeField(default=timezone.now)
    modified_by = models.CharField(max_length=256)
    version_number = models.IntegerField(default=0)
