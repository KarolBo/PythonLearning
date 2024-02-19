from typing import Protocol
from Model import ModelAbs
from pandas import DataFrame
from typing import IO, Any


response = dict[str, str]


class PresenterAbs(Protocol):
    _model: ModelAbs

    def load_data(self, file_path: str) -> response:
        ...

    def get_input_data(self) -> response:
        ...

    def get_analyzed_data(self, option: str) -> response:
        ...
    
    def export_data(self, option: str, file_path: IO[Any]) -> response:
        ...


def celcius_to_kelvin(temperature: float) -> float:
    return temperature + 273.15

def convert_to_scale_0_1(value: float) -> float:
    return value / 100

def compensate_for_sensor_bias(value: float, bias: float = 23) -> float:
    return value + bias


class DataPresenter(PresenterAbs):
    def __init__(self, model: ModelAbs):
        self._model = model

    def load_data(self, file_path: str) -> response:
        try:
            self._model.load_csv(file_path)
            return {
                "header": "Import", 
                "payload": "Data successfully loaded!"
            }
        except:
            return {
                "header": "Error", 
                "payload": "Loading data failed!"
            }

    def get_input_data(self) -> response:
        try:
            data = self._model.get_data()
            return {
                'header': 'Data', 
                'payload': str(data)
            }
        except NameError:
            return {
                'header': 'Error', 
                'payload': 'No data to show!'
            }

    def get_analyzed_data(self, option: str) -> response:
        try:
            data = self._model.get_data()
            processed_data = self._process_data(data, option)
            return {
                'header': 'Data', 
                'payload': str(processed_data)
            }
        except:
            return {
                'header': 'Error', 
                'payload': 'Please load data first!'
            }

    def export_data(self, option: str, file_path: IO[Any]) -> response:
        try:
            data = self._model.get_data()
            processed_data = self._process_data(data, option)
            processed_data.to_csv(file_path, index=False)
            return {
                'header': 'Export', 
                'payload': 'Data exported successfully!'
            }
        except:
            return {
                'header': 'Error', 
                'payload': 'Data export failed!'
            }

    @staticmethod
    def _process_data(data: DataFrame, option: str) -> DataFrame:
        processed_data: list[DataFrame] = []
    
        if option in ("Temperature", "Humidity", "CO2"):
            data = data.loc[data["Sensor"] == option]

        for _, row in data.iterrows():
            processed_row = DataPresenter._process_row(row)
            processed_data.append(processed_row)

        return DataFrame(data=processed_data)
    
    @staticmethod
    def _process_row(row: DataFrame) -> DataFrame:
        sensor: str = row["Sensor"]
        value: float = row["Value"]
        processing_fn = {
            "Temperature": celcius_to_kelvin,
            "Humidity": convert_to_scale_0_1,
            "CO2": compensate_for_sensor_bias,
        }
        row["Value"] = processing_fn[sensor](value)

        return row
