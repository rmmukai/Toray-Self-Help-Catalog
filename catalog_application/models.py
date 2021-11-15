from django.db import models


class SelfHelpArticleManager(models.Manager):
    def self_help_article_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "Please add an appropriate title for this article."
        if len(postData['last_updated_by']) < 1:
            errors['created_by'] = "Please input your name or the person who updated this article."
        if len(postData['description']) < 1:
            errors['description'] = "Please write a short description about the article."
        if len(postData['document_location']) < 1:
            errors['document_location'] = "Please input the document location."
        return errors


class SelfHelpArticle(models.Model):
    title = models.CharField(max_length=100)
    last_updated_by = models.CharField(max_length=50)
    description = models.CharField(max_length=800)
    document_location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SelfHelpArticleManager()