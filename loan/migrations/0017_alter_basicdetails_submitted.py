# Generated by Django 4.1.7 on 2023-05-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loan", "0016_alter_basicdetails_submitted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basicdetails",
            name="submitted",
            field=models.BooleanField(default=False),
        ),
    ]
