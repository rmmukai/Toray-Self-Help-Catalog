from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def desktop_links(request):
    return render(request, 'desktop_links.html')

def admin_page(request):
    return render(request, 'admin_page.html')

def home_page(request):
    return render(request, 'home_page.html')