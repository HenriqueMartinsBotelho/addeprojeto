import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Weather } from '../model/weather.model';

@Injectable({
  providedIn: 'root',
})
export class WeatherService {
  apiUrl = 'http://127.0.0.1:5000/';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    }),
  };

  constructor(private httpClient: HttpClient) {}

  public getWeatherWithFlag(flag: string): Observable<Weather> {
    if (flag == undefined) {
      return this.httpClient.get<Weather>(this.apiUrl);
    }
    return this.httpClient.get<Weather>(this.apiUrl + flag);
  }
}

// fastapi  return this.httpClient.get<Weather>(this.apiUrl + '?q=' + flag);
