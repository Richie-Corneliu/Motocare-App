from datetime import date


class ServiceRecord:
    def __init__(self, date_: date, km: int, service_type: str, cost: float, notes: str = ""):
        self._date = date_
        self._km = km
        self._service_type = service_type
        self._cost = cost
        self._notes = notes

    @property
    def km(self):
        return self._km

    def __str__(self):
        return f"{self._date} | {self._km} km | {self._service_type} | Rp{self._cost:,.0f}"
