from django.db import models

# Create your models here.
NULLABLE = {'null':True, 'blank': True}

class Student(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    patronymic = models.CharField(max_length=150, verbose_name='отчество')
    avatar = models.ImageField(upload_to="students/", verbose_name="аватар", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="учится")

    email = models.CharField(max_length=100, verbose_name='email', unique=True, **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.first_name} {self.last_name} {self.is_active}'


    class Meta:
        verbose_name = 'студент' # Настройка для наименования одного объекта
        verbose_name_plural = 'студенты' # Настройка для наименования набора объектов
        ordering = ('last_name',)
