from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, plate: str, brand: str, model: str, year: int):
        self._plate = plate
        self._brand = brand
        self._model = model
        self._year = year

    @property
    def plate(self):
        return self._plate

    @abstractmethod
    def get_info(self) -> str:
        pass
