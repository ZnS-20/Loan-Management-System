from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    USER_CHOICE = (
        (1,"ADMIN"),
        (2,"USER"),
    )
    first_name = models.CharField(max_length = 60, null=False, blank=False)
    last_name = models.CharField(max_length = 60, null=False, blank=False)
    middle_name = models.CharField(max_length = 60, null=True, blank=True)
    email = models.EmailField(max_length = 254, null=False, blank=False, unique=True)
    phone = models.CharField(max_length = 10, null=False, blank=False)
    password1 = models.CharField(max_length = 10, null=False, blank=False)
    password2 = models.CharField(max_length = 10, null=False, blank=False)
    is_active = models.BooleanField(default = True)
    is_terminated = models.BooleanField(default = False)
    created_by = models.CharField(max_length=5, choices = USER_CHOICE, default = "ADMIN")
    created_date = models.DateField(default = timezone.now)
    modified_by = models.CharField(max_length=5, choices = USER_CHOICE, default = "ADMIN")
    modified_date = models.DateField(default = timezone.now)
    version_number = models.IntegerField(default = 0)
    is_email_verified = models.BooleanField(default = False)

    def __str__(self):
        return self.first_name + ' ' +self.last_name
