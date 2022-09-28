from django.db import models
from django.db.models import Model
from django.urls import reverse

# Create your models here.
class Bike(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    material = models.CharField(max_length=100)
    material_info = models.TextField(max_length=250) 
    description = models.TextField(max_length=250)
    image = models.CharField(max_length=100, default='no image added') 

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'bike_id': self.id})