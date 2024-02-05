from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .forms import RegistrationForm
from .models import Employees


class EmpCatalogListView(ListView):
    template_name = 'employees_catalog/catalog.html'
    model = Employees
    context_object_name = 'top_supervisors'

    def get_queryset(self):
        return Employees.objects.filter(hierarchy_level=0)


@method_decorator(login_required(login_url='login'), name='dispatch')
class CatalogDetailListView(LoginRequiredMixin, ListView):
    template_name = 'employees_catalog/catalog_detail.html'
    model = Employees
    context_object_name = 'employees'
    ordering = ['name']

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.GET.get('order_by')
        order_direction = self.request.GET.get('order_direction', 'asc')
        search_query = self.request.GET.get('search_query')

        if order_by:
            queryset = queryset.order_by(f"{'' if order_direction == 'asc' else '-'}{order_by}")

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(position__icontains=search_query) |
                Q(hire_date__icontains=search_query) |
                Q(salary__icontains=search_query)
            )

        return queryset


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog_detail')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def welcome(request):
    return render(request, 'employees_catalog/welcome.html')
