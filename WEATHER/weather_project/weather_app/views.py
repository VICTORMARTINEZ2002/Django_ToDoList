import datetime

import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    API_KEY = open("C:\\Users\\User\\Documents\\VictorMartinez\\Django_Frist_Steps\\WEATHER\\weather_project\\API_KEY.txt", "r").read()
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

    if(request.method=="POST"):
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None) # Optional

        weather_data1 = fetch_weather(city1, API_KEY, current_weather_url)
        if(city2):
            weather_data2 = fetch_weather(city2, API_KEY, current_weather_url)    
        else:
            weather_data2 = None

        context = {
            "weather_data1":     weather_data1,
            "weather_data2":     weather_data2,
        }
        return render(request, "weather_app/index.html", context)
    else:
        return render(request, "weather_app/index.html")

def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()

    weather_data = {
        "city": city,
        "temperatura": round(response['main']['temp'] - 273.15, 2), # Kelvin
        "description": response['weather'][0]['description'],
        'icon': response['weather'][0]['icon']
    }

    return weather_data 