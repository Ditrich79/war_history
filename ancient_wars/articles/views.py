from django.shortcuts import render
from .models import Article


def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles})
