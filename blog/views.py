from django.shortcuts import render, get_object_or_404, redirect

from .models import Article


def article_list(req):
    queryset = Article.objects.all()
    context = {
        'article_list': queryset
    }

    return render(req, 'blog/article_list.html', context)


def article_detail(req, id):
    article = get_object_or_404(Article, id=id)
    context = {
        'article': article
    }

    return render(req, 'blog/article_detail.html', context)
