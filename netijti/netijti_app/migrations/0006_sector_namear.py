# Generated by Django 4.1.7 on 2023-02-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netijti_app", "0005_alter_result_metadata"),
    ]

    operations = [
        migrations.AddField(
            model_name="sector",
            name="nameAr",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
