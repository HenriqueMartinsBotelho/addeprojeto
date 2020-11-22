import { Component, OnInit } from '@angular/core';
import { WeatherService } from 'src/app/shared/service/weather.service';
import { Weather } from 'src/app/shared/model/weather.model';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css'],
})
export class WeatherComponent implements OnInit {
  weatherData: Weather;
  cityName: string;
  backgroundImg: string;

  constructor(public weatherService: WeatherService) {}

  ngOnInit(): void {
    this.getWeather();
  }

  async getWeather() {
    await this.weatherService
      .getWeatherWithFlag(this.cityName)
      .subscribe((data) => {
        this.weatherData = new Weather(data.celsius, data.name, data.climate);
        this.chooseBackgroundImage(data);
      });
  }

  getCity(city: string) {
    this.cityName = city;
    this.getWeather();
  }

  chooseBackgroundImage(data) {
    // List of all 9 possibilities: https://openweathermap.org/weather-conditions
    if (data.climate === 'Algumas nuvens') {
      this.backgroundImg = '/assets/fewclouds.jpg';
    } else if (data.climate === 'Nuvens dispersas') {
      this.backgroundImg = '/assets/nuvensdispersas.jpg';
    } else if (data.climate === 'Céu limpo') {
      this.backgroundImg = '/assets/ceulimpo.jpg';
    } else if (data.climate === 'Nublado') {
      this.backgroundImg = '/assets/nuvensquebradas.jpg';
    } else if (data.climate === 'Chuva leve') {
      this.backgroundImg = '/assets/chuvadebanho.jpg';
    } else if (data.climate === 'Chuva') {
      this.backgroundImg = '/assets/chuva.jpeg';
    } else if (data.climate === 'Trovoada') {
      this.backgroundImg = '/assets/trovoada.jpg';
    } else if (data.climate === 'Neve') {
      this.backgroundImg = '/assets/neve.jpg';
    } else if (data.climate === 'Névoa') {
      this.backgroundImg = '/assets/nevoa.jpg';
    }
  }
}
