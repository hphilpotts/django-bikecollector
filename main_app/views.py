from cmath import log
import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bike, Accessory
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ComponentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class BikeCreate(LoginRequiredMixin, CreateView):
    model = Bike
    fields = ['make', 'model', 'year', 'material', 'material_info', 'description', 'image']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BikeUpdate(LoginRequiredMixin, UpdateView):
    model = Bike
    fields = ['make', 'model', 'year', 'material', 'material_info', 'description', 'image']

class BikeDelete(LoginRequiredMixin, DeleteView):
    model = Bike
    success_url = '/bikes/'


def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

@login_required
def bikes_index(req):
    bikes = Bike.objects.filter(user = req.user)
    return render(req, 'bikes/index.html', { 'bikes': bikes })

@login_required
def bikes_detail(req, bike_id):
    bike = Bike.objects.get(id = bike_id)
    kit_not_on_bike = Accessory.objects.exclude(id__in = bike.accessories.all().values_list('id'))
        # can't remember how this works, need to get my head around this
    component_form = ComponentForm()
    return render(req, 'bikes/detail.html', {'bike':bike, 'component_form':component_form, 'accessories': kit_not_on_bike })

@login_required
def add_component(req, bike_id):
    form = ComponentForm(req.POST)
    if form.is_valid():
        new_component = form.save(commit=False)
        new_component.bike_id = bike_id
        new_component.save()
    return redirect('detail', bike_id = bike_id)

# CBVs for Accessories CRUD Operations:     

class AccessoryList(LoginRequiredMixin, ListView):
    model = Accessory

class AccessoryDetail(LoginRequiredMixin, DetailView):
    model = Accessory

class AccessoryCreate(LoginRequiredMixin, CreateView):
    model = Accessory
    fields = '__all__'

class AccessoryUpdate(LoginRequiredMixin, UpdateView):
    model = Accessory
    fields = ['brand', 'kit']
class AccessoryDelete(LoginRequiredMixin, DeleteView):
    model = Accessory
    success_url = '/accessories/'

# Associate and Unassociate:
@login_required
def assoc_accessory(req, bike_id, accessory_id):
    Bike.objects.get(id = bike_id).accessories.add(accessory_id)
    return redirect('detail', bike_id = bike_id)

@login_required
def unassoc_accessory(req, bike_id, accessory_id):
    Bike.objects.get(id = bike_id).accessories.remove(accessory_id)
    return redirect('detail', bike_id = bike_id)

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid signup - Please try again later"

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)
    