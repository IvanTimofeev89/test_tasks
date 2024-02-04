
from django.views.generic import ListView

from models import Employees


class EmpCatalog(ListView):
    template_name = 'employees_catalog/catalog.html'
    model = Employees
    context_object_name = 'employees'
