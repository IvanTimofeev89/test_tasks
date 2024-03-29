# Generated by Django 5.0.1 on 2024-02-04 09:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('hire_date', models.DateField()),
                ('salary', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('hierarchy_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subordinates', to='employees_catalog.employees')),
            ],
        ),
    ]
