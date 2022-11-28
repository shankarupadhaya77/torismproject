from django.contrib.auth.models import User
from django.db import models
from .constants import *


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class ImageSlider(TimeStamp):
    image = models.ImageField(upload_to="sliders")
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Category(TimeStamp):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="category")

    def __str__(self):
        return self.title


class Blog(TimeStamp):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blogs")
    video_link = models.CharField(max_length=500, null=True, blank=True)
    details = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Festival(TimeStamp):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="festivals")
    month = models.CharField(max_length=50, choices=MONTHS)
    day = models.CharField(max_length=50, choices=DAYS)
    duration = models.PositiveIntegerField(default=1)
    video_link = models.CharField(max_length=500, null=True, blank=True)
    details = models.TextField()
    significance = models.TextField()

    def __str__(self):
        return self.title


class Heritage(TimeStamp):
    title = models.CharField(max_length=200)
    heritage_type = models.CharField(max_length=200, choices=HERITAGE_TYPE)
    image = models.ImageField(upload_to="cuturalheritages")
    video_link = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=30)
    significance = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.title



class Contact(TimeStamp):



    def __str__(self):
        return self.title

