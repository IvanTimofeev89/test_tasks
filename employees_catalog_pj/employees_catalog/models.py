from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    position = models.CharField(max_length=50, verbose_name='Должность')
    hire_date = models.DateField(verbose_name='Дата приема на работу')
    salary = models.IntegerField(validators=[MinValueValidator(0), ], verbose_name='Заработная плата')
    hierarchy_level = models.IntegerField(validators=[MinValueValidator(0), ], verbose_name='Уровень иерархии')
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                                   blank=True, related_name='subordinates', verbose_name='Руководитель')
    picture = models.ImageField(upload_to='employees_pictures', null=True, blank=True,
                                default="employees_pictures/default.JPG", verbose_name='Фото сотрудника')

    def __str__(self):
        return f'{self.name} - id:{self.id}'
