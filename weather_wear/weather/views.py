
from django.shortcuts import render
import requests
import sqlite3 as sql
from .models import City
from .forms import CityForm
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

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

    city_weather = requests.get(
        url.format(city)).json()  # request the API data and convert the JSON to Python data types
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


def index(request):
    api_id = '845b66b8bb799526bfe36f2e6c41589b'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=845b66b8bb799526bfe36f2e6c41589b'
    # call the API on all the user's favorite cities
    curr_user = request.user
    print("current user is:")
    print(curr_user)
   # cities = City.objects.all()
    cities = City.objects.all().filter(name='destin')

    if request.method == 'POST':
        form = CityForm(request.POST)                    # create a City instance with the entered city name
        if form.is_valid():                                        # for adding error handling
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            #form.save()                                                 # add this to the sqlite City database
    form = CityForm()
    weather_data = []
    for city in cities:
        #request JSON data and converts to python data type
        city_weather = requests.get(url.format(city)).json()
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
