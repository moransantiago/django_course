from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleForm
from .models import Article


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)


class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'blog/article_create.html'

    def form_valid(self, form):
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    template_name = 'blog/article_create.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

    def form_valid(self, form):
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

    def get_success_url(self):
        return reverse('blog:article_list')
