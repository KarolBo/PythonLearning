from typing import Any, Callable
from functools import partial
import requests

from config import API_KEY, CITY, URL

HttpGet = Callable[[str], Any]


class CityNotFoundError(Exception):
    pass


def get(url: str) -> Any:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raise an exception if the request failed
    return response.json()


def get_forecast(http_get: HttpGet, api_key: str, city: str) -> dict[str, Any]:
    response = http_get(URL.format(city, api_key))
    if "main" not in response:
        raise CityNotFoundError(
            f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
        )
    return response


def get_temperature(full_weather_forecast: dict[str, Any]) -> float:
    temperature = full_weather_forecast["main"]["temp"]
    return temperature - 273.15  # convert from Kelvin to Celsius


def get_humidity(full_weather_forecast: dict[str, Any]) -> int:
    return full_weather_forecast["main"]["humidity"]


def get_wind_speed(full_weather_forecast: dict[str, Any]) -> float:
    return full_weather_forecast["wind"]["speed"]


def get_wind_direction(full_weather_forecast: dict[str, Any]) -> int:
    return full_weather_forecast["wind"]["deg"]


def main() -> None:
    get_weather = partial(get_forecast, get, API_KEY)

    weather_forecast = get_weather(CITY)

    print(
        f"The current temperature in {CITY} is {get_temperature(weather_forecast):.1f} °C."
    )
    print(f"The current humidity in {CITY} is {get_humidity(weather_forecast)}%.")
    print(
        f"The current wind speed in {CITY} is {get_wind_speed(weather_forecast) } m/s from direction {get_wind_direction(weather_forecast)} degrees."
    )


if __name__ == "__main__":
    main()
