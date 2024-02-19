from typing import Any, Protocol, Callable

import requests

API_KEY = '132cb366d65744598a9619a04755ee0e'

response_type = dict[str, Any]

class CityNotFoundError(Exception):
    pass


class HttpClient(Protocol):
    def get(self, url: str) -> response_type:
        ...


def get(url: str) -> response_type:
    response = requests.get(url, timeout=5)
    return response.json()


def get_forecast_closure(get: Callable[[str], response_type], api_key: str) -> Callable[[str], response_type]:
    def get_forecast(city: str) -> response_type:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = get(url)
        if "main" not in response:
            raise CityNotFoundError(
                f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
            )
        return response 
    return get_forecast


def temperature(forecast: response_type) -> float:
        temperature = forecast["main"]["temp"]
        return temperature - 273.15 

def humidity(forecast: response_type) -> int:
    return forecast["main"]["humidity"]

def wind_speed(forecast: response_type) -> float:
    return forecast["wind"]["speed"]

def wind_direction(forecast: response_type) -> int:
    return forecast["wind"]["deg"]


def main() -> None:
    get_forecast = get_forecast_closure(get, API_KEY)
    city = "Valencia"
    forecast = get_forecast(city)
    print(f"The current temperature in {city} is {temperature(forecast):.1f} °C.")
    print(f"The current humidity in {city} is {humidity(forecast)}%.")
    print(
        f"The current wind speed in {city} is {wind_speed(forecast)} m/s from direction {wind_direction(forecast)} degrees."
    )


if __name__ == "__main__":
    main()


# As a bonus, can you define another function that allows you to get a weather forecast without having to provide the http getter function and the API key?