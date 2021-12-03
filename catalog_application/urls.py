from django.urls import path
from . import views

urlpatterns = [
    path('home_page', views.home_page),
    path('desktop_links', views.desktop_links),
    path('admin_page', views.admin_page),
    path('admin_page/all_self_help_articles', views.all_self_help_articles),
    path('admin_page/all_self_help_articles/add_self_help_article', views.add_self_help_article),
    path('admin_page/all_self_help_articles/create_article', views.create_article),
    path('admin_page/all_self_help_articles/<self_help_article_id>/edit_articles', views.edit_articles),
    path('admin_page/all_self_help_articles/<self_help_article_id>/update_articles', views.update_articles),
    path('admin_page/all_self_help_articles/<self_help_article_id>/delete_articles', views.delete_articles),
    path('home_page/suggestion_message', views.add_suggestion_message),
    path('home_page/create_suggestion', views.create_suggestion),
]

