import pandas as pd
from typing import Callable
from dataclasses import dataclass


unit_conversion = Callable[[float], float]

class BadOptionException(Exception):
    def __init__(self, option: str) -> None:
        info = f'Option not valid, should be ("All", "Temperature", "Humidity", "CO2"). "{option}" given!'
        super().__init__(info)


@dataclass
class Sensor:
    type: str
    conversion: unit_conversion


class Experiment:
    sensors: dict[str, Sensor] = {}
    ALL: str = "All"

    @classmethod
    def register_sensors(cls):
        cls.sensors['Temperature'] = Sensor('Temperature', lambda x: x + 273.15)
        cls.sensors['Humidity'] = Sensor('Humidity', lambda x: x / 100)
        cls.sensors['CO2'] = Sensor('CO2', lambda x: x + 23)

    def __init__(self, data_path: str) -> None:
        self.register_sensors()
        self._data: pd.DataFrame = pd.read_csv(data_path)

    def _get_filtered_data(self, option: str) -> pd.DataFrame:
        if option != self.ALL:
            return self._data.loc[self._data["Sensor"] == option]
        return self._data

    @classmethod
    def _process_data(cls, data: pd.DataFrame) -> pd.DataFrame:
        processed_data: list[pd.DataFrame] = []
        for _, row in data.iterrows():
            if row["Sensor"] not in cls.sensors:
                continue
            sensor = cls.sensors[row["Sensor"]]
            row["Value"] = sensor.conversion(row["Value"])
            processed_data.append(row)
        return pd.DataFrame(data=processed_data)

    def print_info(self, option: str):
        if option not in self.sensors and option != self.ALL:
            raise BadOptionException(option)
        
        data = self._get_filtered_data(option)
        processed_data = self._process_data(data)

        print(processed_data)


def main() -> None:
    experiment = Experiment("challenge_cohesion/sensor_data.csv")
    experiment.print_info("All")


if __name__ == "__main__":
    main()
