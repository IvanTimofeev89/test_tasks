from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    hire_date = models.DateField()
    salary = models.IntegerField(validators=[MinValueValidator(0), ])
    hierarchy_level = models.IntegerField(validators=[MinValueValidator(0), ])
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                                   blank=True, related_name='subordinates')
    picture = models.ImageField(null=True, blank=True, default=None)


    def __str__(self):
        return f'{self.name}'
