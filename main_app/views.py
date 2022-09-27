from django.shortcuts import render
from django.http import HttpResponse
from .models import Bike

# Create your views here.
def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

# class Bike:
#     def __init__(self, make, model, year, material, description):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.material = material
#         self.description = description

# bikes = [
#     Bike('Fuji', 'Feather', 2020, ['steel', 'Reynolds 520 chromoly'], 'lightweight track-style urban singlspeed bike'),
#     Bike('Condor', 'Acciaio', 2021, ['steel','DZR triple-butted steel with boron'], 'fast and lightweight all-rounder'),
#     Bike('Ribble', 'Gravel Ti', 2022, ['titanium','Gravel Ti triple-butted'], 'durable and responsive gravel bike'),
#     Bike('Colnago', 'C68', 2022, ['carbon','multi-piece carbon fiber, airfoil tube shapes'], "Colnago's latest C-Series flagship road bike"),
# ]

def bikes_index(req):
    bikes = Bike.objects.all() # retrieves all Bike entries and saves into variable
    return render(req, 'bikes/index.html', { 'bikes': bikes })

def bikes_detail(request, bike_id):
    bike = Bike.objects.get(id = bike_id)
    return render(request, 'bikes/detail.html', {'bike':bike})