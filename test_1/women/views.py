from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
# Create your views here.
d = 1
def index(request):
    menu = Women.objects.all()
    if d == 2:
        return redirect(home)
    return render(request, 'women/index.html', {'menu': menu})

def categories(request, catid):
    return HttpResponse(f'<h1> Страница категорий </h1><p>{catid}</p>')

def home(request):
    return render(request, 'women/home.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
