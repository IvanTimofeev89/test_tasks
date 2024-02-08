from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from employees_catalog.models import Employees


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']


class UpdateForm(forms.ModelForm):
    id = forms.IntegerField(required=False, disabled=True, label='Уникальный идентификатор')
    hierarchy_level = forms.IntegerField(required=False, disabled=True, label='Уровень иерархии')

    class Meta:
        model = Employees
        fields = ['id', 'name', 'position', 'hire_date', 'hierarchy_level', 'supervisor', 'picture']
