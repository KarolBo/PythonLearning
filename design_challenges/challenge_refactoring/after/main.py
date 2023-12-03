import argparse
from typing import Any
from functools import partial
import json

from weather import (
    get_complete_forecast,
    http_get,
    get_temperature,
    get_humidity,
    get_wind_speed,
    get_wind_direction,
)

LANG = 'eng'

with open('./challenge_refactoring/after/translations.json') as file:
    text = json.load(file)[LANG]


def define_parser():
    parser = argparse.ArgumentParser(
        description="Get the current weather information for a city"
    )
    parser.add_argument(
        "city", help="Name of the city to get the weather information for"
    )
    parser.add_argument(
        "-c",
        "--conditions",
        dest="conditions",
        metavar="CONDITION",
        nargs="+",
        default=["temperature"],
        choices=["all", "a", "temperature", "t", "humidity", "h", "wind", "w"],
        help="Weather conditions to display. Choose between 'all' or 'a', 'temperature' or 't', "
        "'humidity' or 'h', 'wind' or 'w'.",
    )

    parser.add_argument(
        "--api-key",
        default="132cb366d65744598a9619a04755ee0e",
        help="API key for the OpenWeatherMap API",
    )

    return parser.parse_args()


def forecst_city_condition_to_info(forecast: dict[str, Any], city: str, condition: str) -> str:
    if condition in ["temperature", "t"]:
        temperature = get_temperature(forecast)
        return text['temperature'].format(city=city, temperature=temperature)
    elif condition in ["humidity", "h"]:
        return text['humidity'].format(city=city, humidity=get_humidity(forecast))
    elif condition in ["wind", "w"]:
        return text['wind'].format(city=city, wind_speed=get_wind_speed(forecast), wind_direction=get_wind_direction(forecast))
    
    temperature = get_temperature(forecast)
    return f"The current temperature in {city} is {temperature:.1f} °C. \
             The current humidity in {city} is {get_humidity(forecast)}%. \
             The current wind speed in {city} is {get_wind_speed(forecast)} m/s \
             from direction {get_wind_direction(forecast)} degrees."
    

def main() -> None:
    args = define_parser()
    print()
    print(args)
    print()

    if not args.api_key:
        # That will not happen because of the API default value.
        print("Please provide an API key with the --api-key option.")
        return

    if not args.conditions:
        # This will never happen because temperature is set as the default condition.
        print("Please specify at least one weather condition to display with the --conditions option.")
        return

    # Fetch the data from the OpenMapWeather API
    weather_forecast = get_complete_forecast(
        http_get_fn=http_get, api_key=args.api_key, city=args.city
    )
    if not weather_forecast:
        print("Forecast unavailable")
        return

    condition_to_info = partial(forecst_city_condition_to_info, forecast=weather_forecast, city=args.city)

    for condition in args.conditions:
        print(condition_to_info(condition=condition))

if __name__ == "__main__":
    main()
