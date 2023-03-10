# Generated by Django 4.1.7 on 2023-02-18 10:02

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netijti_app", "0003_result_sector"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="score",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[
                    django.core.validators.MinValueValidator(Decimal("0.00")),
                    django.core.validators.MaxValueValidator(Decimal("20.00")),
                ],
            ),
        ),
    ]
