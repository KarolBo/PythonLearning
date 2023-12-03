from dataclasses import dataclass
from typing import Any
import requests
import asyncio


API_KEY = "132cb366d65744598a9619a04755ee0e"


@dataclass
class UrlTemplateClient:
    template: str

    async def get(self, data: dict[str, Any]) -> Any:
        url = self.template.format(**data)
        response = await asyncio.to_thread(requests.get, url, timeout=5)
        response.raise_for_status()  # Raise an exception if the request failed
        return response.json()


class CityNotFoundError(Exception):
    pass


async def get_capital(country: str) -> str:
    client = UrlTemplateClient(template="https://restcountries.com/v3/name/{country}")
    response = await client.get({"country": country})

    # The API can return multiple matches, so we just return the capital of the first match
    return response[0]["capital"][0]


async def get_forecast(city: str) -> dict[str, Any]:
    client = UrlTemplateClient(
        template=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    )
    response = await client.get({"city": city})
    if "main" not in response:
        raise CityNotFoundError(
            f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
        )
    return response


async def print_forecast_for_capital(country: str) -> None:
    capital = await get_capital(country)
    weather_forecast = await get_forecast(capital)
    print(f"The capital of {country} is {capital}")
    print(
        f"The current temperature in {capital} is {get_temperature(weather_forecast):.1f} °C."
    )


def get_temperature(full_weather_forecast: dict[str, Any]) -> float:
    temperature = full_weather_forecast["main"]["temp"]
    return temperature - 273.15  # convert from Kelvin to Celsius


async def main() -> None:
    countries = ["United States of America", "Australia", "Japan", "France", "Brazil"]

    forecast_requests = [print_forecast_for_capital(country) for country in countries]

    await asyncio.gather(*forecast_requests)


if __name__ == "__main__":
    asyncio.run(main())
