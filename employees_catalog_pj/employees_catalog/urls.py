from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('catalog/', views.EmpCatalogListView.as_view(), name='emp_catalog'),
    path('catalog-detail/', views.CatalogDetailListView.as_view(), name='catalog_detail'),
    path('emp-detail/<int:pk>/', views.EmployeeDetail.as_view(), name='emp_detail'),
]