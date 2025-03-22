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
    views_count = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Введите количество просмотров"
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликованность"
    )
    slug = models.CharField(
        max_length=200,
        verbose_name="slug",
        help_text="человекочитаемая ссылка"
    )


    def __str__(self):
        return f'Курс: {self.title}\nОписание: {self.body}\n'

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"