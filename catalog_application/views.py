from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages


def desktop_links(request):
    return render(request, 'desktop_links.html')


def admin_page(request):
    return render(request, 'admin_page.html')


def home_page(request):
    return render(request, 'home_page.html')


def all_self_help_articles(request):
    context = {
        'self_help_articles': SelfHelpArticle.objects.all()
    }
    return render(request, 'all_self_help_articles.html', context)


def add_self_help_article(request):
    return render(request, 'add_self_help_article.html')


def create_article(request):
    # Error/validator messages found in models.py.
    errors = SelfHelpArticle.objects.self_help_article_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/admin_page/all_self_help_articles/add_self_help_article')
    else:
        new_self_help_articles = SelfHelpArticle.objects.create(
            title=request.POST['title'],
            created_by=request.POST['created_by'],
            description=request.POST['description'],
            document_location=request.POST['document_location'],
        )
        return redirect('/admin_page/all_self_help_articles')

