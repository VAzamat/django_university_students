# Generated by Django 5.1.7 on 2025-03-22 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="patronymic",
            field=models.CharField(
                default=datetime.datetime(
                    2025, 3, 22, 0, 59, 44, 692692, tzinfo=datetime.timezone.utc
                ),
                max_length=150,
                verbose_name="отчество",
            ),
            preserve_default=False,
        ),
    ]
