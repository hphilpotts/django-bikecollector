from django.db import models
from django.db.models import Model
from django.urls import reverse

COMPONENTS = (
    ('G', 'Gearset' ),
    ('W', 'Wheels'),
    ('M', 'Miscellaneous')
)

# Create your models here.
class Accessory(models.Model):
    brand = models.CharField(max_length=50)
    kit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.kit}"

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs= {'pk': self.id })
    class Meta:
        verbose_name_plural = "accessories"
class Bike(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    material = models.CharField(max_length=100)
    material_info = models.TextField(max_length=250) 
    description = models.TextField(max_length=250)
    image = models.CharField(max_length=100, default='no image added')
    accessories = models.ManyToManyField(Accessory) 

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'bike_id': self.id})

    def __str__(self):
        return f"{self.make} {self.model}"

class Component(models.Model):
    comptype = models.CharField(max_length=1, choices=COMPONENTS, default=COMPONENTS[2][0])
    name = models.CharField(max_length=100)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_component_display()}: {self.comptype}"

    # Set order here later:
    # class Meta:
    #   ordering = ['']

