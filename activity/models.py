from django.db import models
from django.urls import reverse

# Create your models here.

class Activity(models.Model):

    description = models.CharField(max_length=256)
    sport = models.CharField(max_length=256)
    time = models.IntegerField()
    duration = models.IntegerField()
    calories = models.IntegerField()
    distance = models.IntegerField()


    def get_absolute_url(self):
        return reverse('activity:detail', kwargs={'pk': self.pk})

class User(models.Model):

    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)