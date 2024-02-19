import pandas as pd
from typing import Protocol


class ModelAbs(Protocol):
    _data: pd.DataFrame | None

    def load_csv(self, file_path: str):
        ...

    def get_data(self) -> pd.DataFrame:
        ...


class DataModel(ModelAbs):
    def __init__(self):
        self._data = None

    def load_csv(self, file_path: str):
        self._data = pd.read_csv(file_path)

    def get_data(self) -> pd.DataFrame:
        if self._data is None:
            raise Exception('Data not loaded!')
        return self._data

