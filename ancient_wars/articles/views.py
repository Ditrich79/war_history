from django.shortcuts import render


def articles(request):
    render(request, 'articles/base.html')
