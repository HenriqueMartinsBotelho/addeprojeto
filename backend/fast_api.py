from typing import Optional
from fastapi import FastAPI
import requests
from geopy.geocoders import Nominatim 
import json
import geocoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

key = "c4dba9a7427787d89ce9356dc48fabf1"



@app.get("/")
def weather(q: Optional[str]=None):
    """
    Recebe uma query 'q' que representa a cidade escolhida, por padrão pega a localização do usuário.
    Retorna Temperatura atual, Cidade e Clima (chovendo, nublado, ensolarado, etc) no formato:
    {
        "celsius": 24.910000000000025,
        "name": "Cássia",
        "climate": "scattered clouds"
    }
    """
    if q == None:
        currentLocation = myLocation()
        weatherData = getWeather(currentLocation)
    else:
        weatherData = getWeather(q)
    return weatherData
        

def getWeather(location):
    complete_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&lang=pt_br&units=metric"+"&appid="+key
    api_link = requests.get(complete_link)
    api_data = api_link.json()
    celsius = round(((api_data['main']['temp'])),2)
    name = api_data['name']
    climate = api_data['weather'][0]['description'].capitalize() 
    return {"celsius": celsius,"name": name, "climate": climate}


def myLocation():
    geolocator = Nominatim(user_agent="geoapiExercises") 
    g = geocoder.ip('me')
    Latitude = str(g.latlng[0])
    Longitude = str(g.latlng[1])
    location = geolocator.reverse(Latitude+","+Longitude)     
    address = location.raw['address'] 
    return address['town'] 







