# Generated by Django 5.1.1 on 2024-10-23 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("borrowings", "0002_initial"),
        ("payments", "0005_rename_status_payment_payment_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="borrowing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments",
                to="borrowings.borrowing",
            ),
        ),
        migrations.AddConstraint(
            model_name="payment",
            constraint=models.UniqueConstraint(
                fields=("payment_type", "borrowing"),
                name="unique_payment_borrowing_and_payment_type",
            ),
        ),
    ]