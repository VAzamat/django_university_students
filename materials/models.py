from django.db import models

# Create your models here.

class Material(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название",
        help_text="Введите название учебного курса"
    )
    body = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание учебного курса"
    )

    def __str__(self):
        return f'Курс: {self.title}\nОписание: {self.body}\n'

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"