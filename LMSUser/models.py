from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class CustomUser(models.Model):
    USER_CHOICE = (
        (1, "ADMIN"),
        (2, "USER"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=10, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_terminated = models.BooleanField(default=False)
    created_by = models.CharField(
        max_length=5, choices=USER_CHOICE, default="ADMIN")
    created_date = models.DateField(default=timezone.now)
    modified_by = models.CharField(
        max_length=5, choices=USER_CHOICE, default="ADMIN")
    modified_date = models.DateField(default=timezone.now)
    version_number = models.IntegerField(default=0)
    is_email_verified = models.BooleanField(default=False)
