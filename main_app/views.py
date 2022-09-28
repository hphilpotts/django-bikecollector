from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bike
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ComponentForm

# Create your views here.

class BikeCreate(CreateView):
    model = Bike
    fields = '__all__'

class BikeUpdate(UpdateView):
    moddel = Bike
    fields = '__all__'

class BikeDelete(DeleteView):
    model = Bike
    success_url = '/bikes/'

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def bikes_index(req):
    bikes = Bike.objects.all() # retrieves all Bike entries and saves into variable
    return render(req, 'bikes/index.html', { 'bikes': bikes })

def bikes_detail(req, bike_id):
    bike = Bike.objects.get(id = bike_id)
    component_form = ComponentForm()
    return render(req, 'bikes/detail.html', {'bike':bike, 'component_form':component_form })

def add_component(req, bike_id):
    form = ComponentForm(req.POST)
    if form.is_valid():
        new_component = form.save(commit=False)
        new_component.bike_id = bike_id
        new_component.save()
    return redirect('detail', bike_id = bike_id)