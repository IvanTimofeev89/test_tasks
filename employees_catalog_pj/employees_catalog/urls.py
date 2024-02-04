from django.urls import path

from . import views


urlpatterns = [
    path('catalog/', views.EmpCatalog.as_view(), name='emp_catalog'),
]