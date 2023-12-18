from django.urls import path
from catalog.views import ContactView, HomeView, CategoryListView, ProductListView, ProductDetailView, \
    BlogListView, BlogDetailView, BlogUpdateView, BlogCreateView, BlogDeleteView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),

    path('catalog/', CategoryListView.as_view(), name='catalog'),

    path('<int:pk>/cat_products/', ProductListView.as_view(), name='all_products'),
    path('<int:pk>/cat_products/create', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('<int:pk>/product_update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/product_delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('blogs/', BlogListView.as_view(), name='all_blogs'),
    path('<int:pk>/blog/', BlogDetailView.as_view(), name='blog'),
    path('blog_create_new/', BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/blog_update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/blog_delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
