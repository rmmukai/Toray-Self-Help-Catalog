from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    return HttpResponse("Hello")

