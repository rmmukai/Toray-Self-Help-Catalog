from django.db import models
# from django.core.files.storage import FileSystemStorage

# fs = FileSystemStorage(location='C:/My Coding Projects/Toray_Project/Toray_Catalog/article_media')


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
    description = models.CharField(max_length=1000)
    document_location = models.CharField(max_length=100)
    article_image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SelfHelpArticleManager()


class SuggestionMessageManager(models.Manager):
    def suggestion_message_validator(self, postData):
        errors = {}
        if len(postData['submitted_by']) < 1:
            errors['submitted_by'] = "Please type your name."
        if len(postData['message']) < 5:
            errors['message'] = "Please type a detailed description of your suggestion."
        return errors


class SuggestionMessage(models.Model):
    submitted_by = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SuggestionMessageManager()
