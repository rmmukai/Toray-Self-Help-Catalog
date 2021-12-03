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
            last_updated_by=request.POST['last_updated_by'],
            description=request.POST['description'],
            document_location=request.POST['document_location'],
        )
        return redirect('/admin_page/all_self_help_articles')


def edit_articles(request, self_help_article_id):
    db_articles = SelfHelpArticle.objects.get(id=self_help_article_id)

    context = {
        'self_help_articles': db_articles
    }
    return render(request, 'edit_self_help_articles.html', context)


def update_articles(request, self_help_article_id):
    db_self_help_article = SelfHelpArticle.objects.get(id=self_help_article_id)

    errors = SelfHelpArticle.objects.self_help_article_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/admin_page/all_self_help_articles/{db_self_help_article.id}/edit_articles')
    else:
        # data from the post into variable
        post_title = request.POST.get('title')
        post_last_updated_by = request.POST.get('last_updated_by')
        post_description = request.POST.get('description')
        post_document_location = request.POST.get('document_location')

        # Update the fields in the database object.
        db_self_help_article.title = post_title
        db_self_help_article.last_updated_by = post_last_updated_by
        db_self_help_article.description = post_description
        db_self_help_article.document_location = post_document_location

        db_self_help_article.save()

        return redirect('/admin_page/all_self_help_articles')

def delete_articles(request, self_help_article_id):
    self_help_article = SelfHelpArticle.objects.get(id=self_help_article_id)
    self_help_article.delete()

    return redirect('/admin_page/all_self_help_articles')

def add_suggestion_message(request):
    return render(request, 'suggestion_message.html')

def create_suggestion(request ):
    # Error/validator messages found in models.py.
    errors = SuggestionMessage.objects.suggestion_message_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/home_page/suggestion_message')
    else:
        new_suggestion = SuggestionMessage.objects.create(
            submitted_by=request.POST['submitted_by'],
            message=request.POST['message'],
        )
        return redirect('')