import requests
import sqlite3 as sql
from .models import City, Outfit
from .forms import CityForm
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

class AboutView(TemplateView):
    template_name = "about.html"


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def guest(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=845b66b8bb799526bfe36f2e6c41589b'
    city = "Tallahassee"                                        # the default value to display for users
    if request.method == 'POST':
        city = request.POST['city']
    city_weather = requests.get(url.format(city)).json()        # request the API data and convert the JSON to Python data types
    if city_weather['cod'] == "404":
        messages.error(request, "City not found.")
        return redirect('/')
    try:
        p = city_weather['weather'][0]['snow']
        prec_type = 'snow'
    except:
        prec_type = 'main'
    try:
        p = city_weather['weather'][0]['rain']
        prec_type = "rain"
    except:
        prec_type = 'main'

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'precipitation': city_weather['weather'][0][prec_type],
        'humidity': city_weather['main']['humidity'],
        'description': city_weather['weather'][0]['description'],
        'wind': city_weather['wind']['speed'],
        'icon': city_weather['weather'][0]['icon']
    }
    temperature = weather['temperature']
    if weather['wind'] > 50:
        temperature = temperature -10
    elif weather['wind'] > 20:
        temperature = temperature -5
    if weather['humidity'] > 50:
        temperature = temperature +5
    elif weather['humidity'] < 30:
        temperature = temperature -5
    if prec_type == 'rain':
        print("ATTN: Tell user to bring an umbrella")
    elif prec_type == 'snow':
        print("ATTN: Tell user to wear a coat")

    temperature = round(temperature/10)*10
    outfit = Outfit.objects.get(temp = temperature)
    context = {'weather' : weather, 'outfit' : outfit}

    return render(request, 'guest.html', context)               # returns the guest.html template


def delete(request):
    if request.method == 'POST':
        city = request.POST['pk']
        City.objects.get(name = city, owner = request.user).delete()
        messages.info(request, "Deletion successful.")
        return HttpResponseRedirect('index')
    else:
        messages.error(request, "Deletion unsuccessful.")
        return HttpResponseRedirect('index')


def index(request):
    api_id = '845b66b8bb799526bfe36f2e6c41589b'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=845b66b8bb799526bfe36f2e6c41589b'
    cities = City.objects.all().filter(owner=request.user)  # call the API on all the user's favorite cities

    if request.method == 'POST':

        form = CityForm(request.POST)                        # create a City instance with the entered city name
        if form.is_valid():                                  # add error handling
            try:
                instance = form.save(commit=False)
                city_weather = requests.get(url.format(instance.name)).json()
                if city_weather['cod'] == "404":
                    messages.error(request, "City not found.")
                    return redirect('index')

                instance.name=instance.name.lower()
                instance.owner = request.user
                instance.save()
            except:
                messages.error(request, "City already in favorites. Add a new city.")
                return redirect('index')
        else:
            messages.error(request, "City not added")
            return redirect('index')

    form = CityForm()
    weather_data = []
    outfit_data = []

    for city in cities:
            city_weather = requests.get(url.format(city)).json()        #request JSON data and converts to python data type
            try:
                p = city_weather['weather'][0]['snow']
                prec_type = 'snow'
            except:
                prec_type = 'main'
            try:
                p = city_weather['weather'][0]['rain']
                prec_type = "rain"
            except:
                prec_type = 'main'

            weather = {                                                 #created the weather variable
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'humidity' : city_weather['main']['humidity'],
                'precipitation': city_weather['weather'][0][prec_type],
                'description' : city_weather['weather'][0]['description'],
                'wind': city_weather['wind']['speed'],
                'icon' : city_weather['weather'][0]['icon']
            }
            # map the temp to a value that exists in the database by rounding to nearest 10
            weather_data.append(weather)
            temperature = round(weather['temperature'] / 10) * 10
            outfit = Outfit.objects.get(temp=temperature)
            outfit_data.append(outfit)

    mylist = zip(weather_data, outfit_data)
    context = {'mylist' : mylist, 'form' : form}


    return render(request, 'weather/index.html', context)
