# Generated by Django 5.1.7 on 2025-03-24 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0003_student_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
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
                (
                    "title",
                    models.CharField(
                        help_text="Введите название учебного предмета",
                        max_length=150,
                        verbose_name="название",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание учебного предмета",
                        verbose_name="описание",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.student",
                        verbose_name="студент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Предмет",
                "verbose_name_plural": "Предметы",
                "ordering": ("title",),
            },
        ),
    ]
