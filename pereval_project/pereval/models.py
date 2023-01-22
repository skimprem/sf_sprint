from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .resources import *

# Create your models here.

class PerevalUser(models.Model):
    phone = models.CharField(max_length=128, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    firstname = models.CharField(max_length=255, default=None)
    lastname = models.CharField(max_length=255, default=None)
    middlename = models.CharField(max_length=255, default=None)


class Coords(models.Model):
    add_time = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(default=None, null=True)
    longitude = models.FloatField(default=None, null=True)
    height = models.IntegerField(default=None, null=True)

class Image(models.Model):
    add_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    data = models.CharField(max_length=255)


class Pereval(models.Model):
    user = models.ForeignKey(PerevalUser, on_delete=models.CASCADE, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUSES, default='new')
    title = models.CharField(max_length=255, default='', help_text='Enter title', null=True, blank=True)
    other_titles = models.CharField(max_length=255, default='', help_text='Enter other title', null=True, blank=True)
    beautyTitle = models.CharField(max_length=255, default='', help_text='Enter beauty title', null=True, blank=True)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE, null=True)
    connect = models.CharField(max_length=255, default='', null=True, blank=True)
    images = models.ManyToManyField(Image, through="PerevalImages")
    winter = models.CharField(max_length=2, choices=LEVELS, blank=True, default='')
    summer = models.CharField(max_length=2, choices=LEVELS, blank=True, default='')
    autumn = models.CharField(max_length=2, choices=LEVELS, blank=True, default='')
    spring = models.CharField(max_length=2, choices=LEVELS, blank=True, default='')

class PerevalImages(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE)
