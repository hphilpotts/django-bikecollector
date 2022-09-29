from django.contrib import admin
from .models import Bike, Component, Accessory

# Register your models here.
admin.site.register(Bike)
admin.site.register(Component)
admin.site.register(Accessory)
