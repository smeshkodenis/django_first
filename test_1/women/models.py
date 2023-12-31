from django.db import models


# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    new_info = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
