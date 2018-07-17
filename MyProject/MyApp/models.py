from django.db import models

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=264)
    age = models.IntegerField()
    email = models.EmailField(max_length=264,unique=True)
    occupation = models.CharField(max_length=128)
    place = models.CharField(max_length=128)
