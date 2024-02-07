from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path

from employees_catalog_pj import settings
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', LoginView.as_view(), name='login'),
    path('login_admin/', LoginView.as_view(template_name="registration/login_admin.html"), name='login_admin'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('catalog/', views.EmpCatalogListView.as_view(), name='emp_catalog'),
    path('catalog_detail/', views.CatalogDetailListView.as_view(), name='catalog_detail'),
    path('emp_detail/<int:pk>/', views.EmployeeDetail.as_view(), name='emp_detail'),
    path('emp_update/<int:pk>/', views.UpdateEmp.as_view(), name='emp_update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
