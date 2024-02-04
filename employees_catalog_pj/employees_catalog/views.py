
from django.views.generic import ListView

from .models import Employees


class EmpCatalogListView(ListView):
    template_name = 'employees_catalog/catalog.html'
    model = Employees
    context_object_name = 'top_supervisors'

    def get_queryset(self):
        return Employees.objects.filter(hierarchy_level=0)