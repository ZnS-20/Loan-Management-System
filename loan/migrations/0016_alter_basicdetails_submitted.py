# Generated by Django 4.1.7 on 2023-05-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loan", "0015_basicdetails_submitted_alter_basicdetails_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basicdetails",
            name="submitted",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
