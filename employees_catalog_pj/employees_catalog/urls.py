from django.urls import path

from . import views


urlpatterns = [
    path('catalog/', views.EmpCatalogListView.as_view(), name='emp_catalog'),
    path('catalog-detail/', views.CatalogDetailListView.as_view(), name='catalog_detail'),
]