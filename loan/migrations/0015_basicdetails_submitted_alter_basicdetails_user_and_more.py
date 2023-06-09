# Generated by Django 4.1.7 on 2023-04-29 10:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("LMSUser", "0008_remove_customuser_password1_and_more"),
        ("loan", "0014_loantypes_down_payment_loantypes_interest_rate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="basicdetails",
            name="submitted",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="basicdetails",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="LMSUser.customuser",
            ),
        ),
        migrations.AlterField(
            model_name="loantypes",
            name="interest_rate",
            field=models.DecimalField(
                decimal_places=2,
                default=7.2,
                max_digits=4,
                validators=[
                    django.core.validators.MinValueValidator(7.1),
                    django.core.validators.MaxValueValidator(15.0),
                ],
            ),
        ),
    ]
