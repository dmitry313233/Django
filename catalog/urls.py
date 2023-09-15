from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .apps import CatalogConfig
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView, ProductDetailView

app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.product, name='products'),
    path('create/', ProductCreateView.as_view(), name='create'),  # form  или здесь писать cache_page()
    path('detail/<int:pk>/', cache_page(90)(ProductDetailView.as_view()), name='product_detail'),    # form  или здесь писать cache_page()
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),  # form
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete')    # form
]