from pyexpat import model
from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=100)
    temp = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.city