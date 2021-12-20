from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Friends(models.Model):
    friends1 = models.CharField(max_length=50)
    friends2 = models.CharField(max_length=50)


class userProfiles(models.Model):
    username = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    DOB = models.DateField()
    profile_pics = models.ImageField(upload_to="Profies", blank=True)


class posts(models.Model):
    owner_username = models.CharField(max_length=50, blank=True)
    privacy = models.CharField(max_length=10)
    captions = models.TextField(blank=True)
    post_image = models.ImageField(upload_to="Posts", blank=True)
