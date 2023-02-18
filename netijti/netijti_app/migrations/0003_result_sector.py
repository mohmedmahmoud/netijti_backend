# Generated by Django 4.1.7 on 2023-02-18 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("netijti_app", "0002_result_metadata"),
    ]

    operations = [
        migrations.AddField(
            model_name="result",
            name="sector",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="netijti_app.sector",
            ),
            preserve_default=False,
        ),
    ]