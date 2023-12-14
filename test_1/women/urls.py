from django.urls import path

from .views import *



urlpatterns = [
    path('', index),
    path('cats/<int:catid>/', categories),
    path('home', home)

]
handler404 = pageNotFound

