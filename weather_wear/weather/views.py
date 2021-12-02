
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import requests
import sqlite3 as sql
from .models import City
from .forms import CityForm
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.contrib import messages

class AboutView(TemplateView):
    template_name = "about.html"

class GuestView(TemplateView):
    template_name = "guest.html"


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def guest(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=845b66b8bb799526bfe36f2e6c41589b'
    city = "Melbourne"
    if request.method == 'POST':
        print("we entered a POST method on guest page")
        city = request.POST['city']
    city_weather = requests.get(url.format(city)).json()  # request the API data and convert the JSON to Python data types
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'humidity': city_weather['main']['humidity'],
        'description': city_weather['weather'][0]['description'],
        'wind': city_weather['wind']['speed'],
        'icon': city_weather['weather'][0]['icon']
    }
    context = {'weather' : weather}
    return render(request, 'guest.html', context)  # returns the guest.html template


def delete(request):
    if request.method == 'POST':
        city = request.POST['pk']
        City.objects.get(name = city).delete()
        #return render(request, views.index)
        messages.info(request, "Deletion successful.")
        return HttpResponseRedirect('index')
    else:
        messages.error(request, "Deletion unsuccessful.")
        return HttpResponseRedirect('index')

def index(request):
    api_id = '845b66b8bb799526bfe36f2e6c41589b'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=845b66b8bb799526bfe36f2e6c41589b'
    # call the API on all the user's favorite cities
    cities = City.objects.all().filter(owner=request.user)

    if request.method == 'POST':
        form = CityForm(request.POST)                    # create a City instance with the entered city name
        if form.is_valid():                              # add error handling
            instance = form.save(commit=False)
            if True in [char.isdigit() for char in instance.name]:
                messages.error(request, "City name must contain only letters")
                return redirect('index')
            city_weather = requests.get(url.format(instance.name)).json()
            if city_weather['cod'] == "404":
                messages.error(request, "City not found.")
                return redirect('index')
            instance.name=instance.name.lower()
            instance.owner = request.user
            instance.save()

            print("INStance saved")             # debug
    form = CityForm()
    weather_data = []

    for city in cities:
            #request JSON data and converts to python data type
            city_weather = requests.get(url.format(city)).json()
            """
            # code should NEVER arrive here
            if city_weather['cod'] == "404":
                messages.error(request, "City not found.")
                return redirect('index')
            """


            #created the weather variable
            weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'humidity' : city_weather['main']['humidity'],
                'description' : city_weather['weather'][0]['description'],
                'wind': city_weather['wind']['speed'],
                'icon' : city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)
    context = {'weather_data' : weather_data, 'form' : form}

    with sql.connect("weather/OUTFITS.db") as con:
        cur = con.cursor()
        sql_select_query = '''SELECT * FROM OUTFITS'''
        cur.execute(sql_select_query)
        con.commit()
    con.close()


    return render(request, 'weather/index.html', context)
