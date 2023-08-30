from django.urls import path

from bloc_record.apps import BlocRecordConfig
from bloc_record.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlocRecordConfig.name




urlpatterns = [
    path('blog_create/', BlogCreateView.as_view(), name='blog_record_create'),  # Это переход в строке браузера
    path('blog_home/', BlogListView.as_view(), name='blog_record_list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),  # счетчик
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),  # редактрование
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_confirm_delete')  # удаление
]