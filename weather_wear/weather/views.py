from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    api_id = '845b66b8bb799526bfe36f2e6c41589b'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=845b66b8bb799526bfe36f2e6c41589b'
    # call the API on all the user's favorite cities
    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []
    for city in cities:
        #request JSON data and converts to python data type
        city_weather = requests.get(url.format(city)).json()
        #created the weather variable
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather/index.html', context)