# Generated by Django 4.1.7 on 2023-03-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=60)),
                ("last_name", models.CharField(max_length=60)),
                ("middle_name", models.CharField(blank=True, max_length=60, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=10)),
                ("password1", models.CharField(max_length=10)),
                ("password2", models.CharField(max_length=10)),
                ("is_active", models.BooleanField()),
                ("is_terminated", models.BooleanField()),
                ("created_date", models.DateField()),
                ("modified_date", models.DateField()),
                ("version_number", models.IntegerField()),
                ("is_email_verified", models.IntegerField()),
            ],
        ),
    ]
