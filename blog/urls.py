# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article-list'),
    path('create/', views.article_create, name='article-create'),
    path('<int:pk>/', views.article_detail, name='article-detail'),
    path('<int:pk>/edit/', views.article_edit, name='article-edit'),
    path('<int:pk>/delete/', views.article_confirm_delete, name='article-delete'),  # New URL for delete
]

