from typing import Any, Protocol
import requests

API_KEY = '132cb366d65744598a9619a04755ee0e'


class CityNotFoundError(Exception):
    pass


class HttpClient(Protocol):
    @staticmethod
    def get( url: str) -> requests.Response:
        ...


class RequestClient(HttpClient):
    @staticmethod
    def get(url: str) -> requests.Response:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response


class WeatherService:
    def __init__(self, api_key: str, client: HttpClient) -> None:
        self.api_key = api_key
        self.client = client
        self.full_weather_forecast: dict[str, Any] = {}

    def retrieve_forecast(self, city: str) -> None:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = self.client.get(url).json()
        if "main" not in response:
            raise CityNotFoundError(
                f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
            )
        self.full_weather_forecast = response

    @property
    def temperature(self):
        return self.full_weather_forecast["main"]["temp"] - 273.15
    
    @property
    def humidity(self):
        return self.full_weather_forecast["main"]["humidity"]
    
    @property
    def wind_speed(self):
        return self.full_weather_forecast["wind"]["speed"]
    
    @property
    def wind_direction(self):
        return self.full_weather_forecast["wind"]["deg"]


def main() -> None:
    city = "Adliswil"

    service = WeatherService(api_key=API_KEY, client=RequestClient)
    service.retrieve_forecast(city=city)
    print(f"The current temperature in {city} is {service.temperature:.1f} °C.")
    print(f"The current humidity in {city} is {service.humidity}%.")
    print(
        f"The current wind speed in {city} is {service.wind_speed} m/s from direction {service.wind_direction} degrees."
    )


if __name__ == "__main__":
    main()
