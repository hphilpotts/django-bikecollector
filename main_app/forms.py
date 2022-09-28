from django.forms import ModelForm
from .models import Component

class ComponentForm(ModelForm):
    class Meta:
        model = Component
        fields = ['comptype', 'name']