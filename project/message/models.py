from django.db import models

# Create your models here.

class Message(models.Model):
    messfile = models.FileField(upload_to='documents/%Y/%m/%d')
    messname = models.CharField(max_length=500)
    messenger = models.CharField(max_length=500)
    race = models.CharField(max_length=500)
    messabout = models.CharField(max_length=2000)
    money = models.CharField(max_length=2000)
    messtest = models.CharField(max_length=1000)
    notes = models.TextField(blank=True)