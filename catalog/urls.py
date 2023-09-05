from django.urls import path

from . import views
from .apps import CatalogConfig
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView, ProductDetailView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.product, name='products'),
    path('create/', ProductCreateView.as_view(), name='create'),  # form
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),    # form
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),  # form
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete')    # form
]