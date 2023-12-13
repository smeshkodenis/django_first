from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    menu = Women.objects.all()
    return render(request, 'women/index.html', {'menu': menu})

def categories(request, catid):
    return HttpResponse(f'<h1> Страница категорий </h1><p>{catid}</p>')

