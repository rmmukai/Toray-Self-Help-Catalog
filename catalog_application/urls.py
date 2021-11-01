from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('admin_page', views.admin_page),
    path('desktop_links', views.desktop_links),
]