from typing import Any, Callable

import requests


API_KEY = '132cb366d65744598a9619a04755ee0e'

forecast_dict = dict[str, Any]
forecast_parser = Callable[[forecast_dict], Any]


class CityNotFoundError(Exception):
    pass


class WeatherService:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.full_weather_forecast: forecast_dict = {}


    def retrieve_forecast(self, city: str) -> None:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url, timeout=5).json()
        if "main" not in response:
            raise CityNotFoundError(
                f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
            )

        self.full_weather_forecast = response


    @property
    def temperature(self):
        return self.full_weather_forecast["main"]["temp"] - 273.15


if __name__ == "__main__":
    weather_service = WeatherService(api_key=API_KEY)
    city = "Adliswil"
    weather_service.retrieve_forecast(city)
    print(f"The current temperature in {city} is {weather_service.temperature:.1f} °C.")
    print()
