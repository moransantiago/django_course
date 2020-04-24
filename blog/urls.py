from django.urls import path

from blog.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('update/<int:id>', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:id>', ArticleDeleteView.as_view(), name='article_delete'),
]
