from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bike, Accessory
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ComponentForm

# Create your views here.

class BikeCreate(CreateView):
    model = Bike
    fields = ['make', 'model', 'year', 'material', 'material_info', 'description', 'image']

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
    kit_not_on_bike = Accessory.objects.exclude(id__in = bike.accessories.all().values_list('id'))
        # can't remember how this works, need to get my head around this
    component_form = ComponentForm()
    return render(req, 'bikes/detail.html', {'bike':bike, 'component_form':component_form, 'accessories': kit_not_on_bike })

def add_component(req, bike_id):
    form = ComponentForm(req.POST)
    if form.is_valid():
        new_component = form.save(commit=False)
        new_component.bike_id = bike_id
        new_component.save()
    return redirect('detail', bike_id = bike_id)

# CBVs for Accessories CRUD Operations:     

class AccessoryList(ListView):
    model = Accessory

class AccessoryDetail(DetailView):
    model = Accessory

class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'

class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ['brand', 'kit']
class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'

# Associate and Unassociate:
def assoc_accessory(req, bike_id, accessory_id):
    Bike.objects.get(id = bike_id).accessories.add(accessory_id)
    return redirect('detail', bike_id = bike_id)

def unassoc_accessory(req, bike_id, accessory_id):
    Bike.objects.get(id = bike_id).accessories.remove(accessory_id)
    return redirect('detail', bike_id = bike_id)
    