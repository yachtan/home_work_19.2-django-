from django.urls import path
from catalog.views import home, contacts, catalog, all_products, product
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', catalog, name='catalog'),
    path('<int:pk>/all_products/', all_products, name='all_products'),
    path('<int:pk>/product/', product, name='product')
]
