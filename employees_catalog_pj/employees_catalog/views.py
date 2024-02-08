from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView

from .forms import RegistrationForm, UpdateForm
from .models import Employees

QUERY_LIMIT = 100

class EmpCatalogListView(ListView):
    template_name = 'employees_catalog/catalog.html'
    model = Employees
    context_object_name = 'top_supervisors'

    def get_queryset(self):
        if QUERY_LIMIT:
            return Employees.objects.filter(hierarchy_level=0)[:QUERY_LIMIT]
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
        if QUERY_LIMIT:
            return queryset[:QUERY_LIMIT]
        return queryset


def is_admin(user):
    return user.is_staff


@method_decorator(user_passes_test(is_admin, login_url='login_admin', redirect_field_name='next'), name='dispatch')
class UpdateEmp(UpdateView):
    model = Employees
    template_name = 'employees_catalog/emp_update.html'
    form_class = UpdateForm

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', reverse_lazy('welcome')).replace('emp_update', 'emp_detail')


@method_decorator(login_required(login_url='login', redirect_field_name='next'), name='dispatch')
class EmployeeDetail(DetailView):
    template_name = 'employees_catalog/emp_detail.html'
    model = Employees
    context_object_name = 'employee'


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
