# Generated by Django 4.1.7 on 2023-04-26 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("loan", "0008_alter_documents_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="documents",
            name="loan_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="loan.basicdetails",
            ),
        ),
    ]
