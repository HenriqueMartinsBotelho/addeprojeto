from flask import Flask
from geopy.geocoders import Nominatim 
import geocoder
import requests
from flask_cors import CORS
from flask_caching import Cache
import time
import json


app = Flask(__name__)
CORS(app)
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)
key = "c4dba9a7427787d89ce9356dc48fabf1"

config = {
    "DEBUG": True,          
    "CACHE_TYPE": "simple", 
    "CACHE_DEFAULT_TIMEOUT": 300
}


@app.route("/")
@cache.cached(timeout=900)
def default():
    #time.sleep(10) para ver o cache funcionando 
    currentLocation = myLocation()
    weatherData = getWeather(currentLocation)
    return weatherData

@app.route("/<city>")
@cache.cached(timeout=900)
def weather(city):
    #time.sleep(10) para ver o cache funcionando 
    weatherData = getWeather(city)
    return weatherData


#roda não funcionou ainda
@app.route("/mes/<city>")
def weathermonth(city):
  periodData = getWeatherPeriod(city,1,10)
  return periodData
 

def getWeather(location):
    complete_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&lang=pt_br&units=metric"+"&appid="+key
    api_link = requests.get(complete_link)
    api_data = api_link.json()
    celsius = round(((api_data['main']['temp'])),2)
    name = api_data['name']
    climate = api_data['weather'][0]['description'].capitalize() 
    return {"celsius": celsius,"name": name, "climate": climate}


# Extra: Pegar tempo por periodo
"""
def getWeatherPeriod(location,start,end):
  period = []
  for i in range(start,end):
    complete_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&month=11&day="+str(i)+"&lang=pt_br&units=metric"+"&appid="+key
    api_link = requests.get(complete_link)
    api_data = api_link.json()
    celsius = round(((api_data['main']['temp'])),2)
    name = api_data['name']
    climate = api_data['weather'][0]['description'].capitalize() 
    period.append({"celsius": celsius,"name": name, "climate": climate})
  return json.dumps(period)
"""


def myLocation():
    geolocator = Nominatim(user_agent="geoapiExercises") 
    g = geocoder.ip('me')
    Latitude = str(g.latlng[0])
    Longitude = str(g.latlng[1])
    location = geolocator.reverse(Latitude+","+Longitude)     
    address = location.raw['address'] 
    return address['town'] 

app.config.from_mapping(config)
app.run() 
  