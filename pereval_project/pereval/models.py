from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

STATUSES = [
    ('new', 'new'),
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('rejected', 'rejected'),
]

LEVELS = [
    ('winter', ''),
    ('summer', ''),
    ('autumn', ''),
    ('spring', ''),
]

class PerevalUser(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    firstname = models.CharField(max_length=255, default=None)
    lastname = models.CharField(max_length=255, default=None)
    middlename = models.CharField(max_length=255, default=None)


class Coords(models.Model):
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    height = models.IntegerField(default=None)

class Image(models.Model):
    name = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)

class Pereval(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, choices=STATUSES, default=None)
    title = models.CharField(max_length=255, default=None)
    other_titles = models.CharField(max_length=255, default=None)
    beautyTitle = models.CharField(max_length=255, default=None)
    level = models.CharField(max_length=6, choices=LEVELS, default=None)
    coord_id = models.ForeignKey(Coords, on_delete=models.CASCADE)
    connect = models.CharField(max_length=255, default="")
    images = models.ManyToManyField(Image, through="PerevalImages")

    # raw_data = models.JSONField(encoder="")
    # images = models.JSONField(encoder="")

class PerevalImages(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE)
