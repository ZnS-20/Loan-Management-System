# Generated by Django 4.1.7 on 2023-03-26 17:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("LMSUser", "0008_remove_customuser_password1_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="LoanTypes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "modified_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("version_number", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="BasicDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address1", models.CharField(max_length=512)),
                ("zipcode1", models.CharField(max_length=6)),
                ("address2", models.CharField(max_length=512)),
                ("zipcode2", models.CharField(max_length=6)),
                (
                    "salary_type",
                    models.CharField(
                        choices=[(2, "Bussiness"), (1, "Salaried"), (3, "Student")],
                        max_length=15,
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "modified_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("version_number", models.IntegerField(default=0)),
                (
                    "loan_type",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="loan.loantypes",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="LMSUser.customuser",
                    ),
                ),
            ],
        ),
    ]
