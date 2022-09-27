from django.db import models
from django.db.models import Model

# Create your models here.
class Bike(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    material = models.CharField(max_length=100)
    material_info = models.TextField(max_length=250) 
    description = models.TextField(max_length=250) 

# class Bike:
#     def __init__(self, make, model, year, material, description):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.material = material
#         self.description = description