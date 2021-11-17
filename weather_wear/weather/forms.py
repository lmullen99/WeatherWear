from django import forms
from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        }

class SearchForm(forms.Form):
    fields = ['name']
    widgets = {
        'name': TextInput(attrs={'class': 'input', 'placeholder': ' Enter a City Name'}),
    }

