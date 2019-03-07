from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    ArticleUpdateView,
)

app_name = 'article'

urlpatterns = [
    path('', ArticleListView.as_view(template_name='article/article_list.html'), name='article_list'),
    path('create', ArticleCreateView.as_view(template_name='article/article_create.html'), name='article_create'),
    path('<int:pk>/update', ArticleUpdateView.as_view(template_name='article/article_update_form.html'), name='article_update'),
    path('<int:pk>', ArticleDetailView.as_view(template_name='article/article_detail.html'), name='article_detail'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(template_name='article/article_confirm_delete.html'), name='article_delete'),
]
