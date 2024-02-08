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
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if self.supervisor and (self.hierarchy_level != self.supervisor.hierarchy_level + 1):
            self.hierarchy_level = self.supervisor.hierarchy_level + 1
            if self.subordinates.all():
                _recursive_hierarchy_update(subordinates=self.subordinates.all(),
                                            boss_hierarchy_level=self.hierarchy_level)
        super().save(*args, **kwargs)


def _recursive_hierarchy_update(subordinates: Employees, boss_hierarchy_level: int) -> None:
    for subordinate in subordinates:
        subordinate.hierarchy_level = boss_hierarchy_level + 1
        subordinate.save()
        if subordinate.subordinates.all():
            _recursive_hierarchy_update(subordinate.subordinates.all(), subordinate.hierarchy_level)
