from django.urls import path

from .views import *



urlpatterns = [
    path('', index),
    path('cats/<int:catid>/', categories),
    path('home', home),
    path('contacts', contacts, name='contacts'),
    path('about', home),
    path('news', news, name='news'),


]
handler404 = pageNotFound

