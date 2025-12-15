from datetime import date
from models.vehicle import Vehicle
from models.service_record import ServiceRecord


class Motorcycle(Vehicle):
    def __init__(self, plate: str, brand: str, model: str, year: int, current_km: int):
        super().__init__(plate, brand, model, year)
        self._current_km = current_km
        self._service_records: list[ServiceRecord] = []

    def add_service(self, record: ServiceRecord):
        self._service_records.append(record)
        self._current_km = record.km  # update otomatis

    def update_service(self, index: int, date_: date, km: int, service_type: str, cost: float, notes: str = ""):
        """Update satu record servis berdasarkan index."""
        if index < 0 or index >= len(self._service_records):
            raise IndexError("Index service record tidak valid")

        self._service_records[index] = ServiceRecord(date_, km, service_type, cost, notes)
        # update current_km mengikuti servis terakhir jika ini adalah record terakhir
        if index == len(self._service_records) - 1:
            self._current_km = km

    def get_last_service(self):
        if not self._service_records:
            return None
        return self._service_records[-1]

    def get_info(self) -> str:
        return f"[{self._plate}] {self._brand} {self._model} ({self._year}) - {self._current_km} km"

    @property
    def service_records(self):
        # di sini boleh return langsung (bukan copy) kalau kamu mau edit di tempat
        return self._service_records
