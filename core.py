from models.motorcycle import Motorcycle
from models.service_record import ServiceRecord
from datetime import date


class User:
    def __init__(self, name: str):
        self._name = name
        self._motorcycles: list[Motorcycle] = []

    def add_motorcycle(self, mc: Motorcycle):
        self._motorcycles.append(mc)

    def get_motorcycle_by_plate(self, plate: str):
        for mc in self._motorcycles:
            if mc.plate == plate:
                return mc
        return None

    def remove_motorcycle_by_plate(self, plate: str) -> bool:
        """Hapus motor berdasarkan plat. Return True kalau ada yang dihapus."""
        for i, mc in enumerate(self._motorcycles):
            if mc.plate == plate:
                del self._motorcycles[i]
                return True
        return False

    @property
    def motorcycles(self):
        return list(self._motorcycles)

class MotoCareApp:
    def __init__(self, user: User):
        self._user = user

    def add_motorcycle(self, plate, brand, model, year, current_km):
        mc = Motorcycle(plate, brand, model, year, current_km)
        self._user.add_motorcycle(mc)

    def add_service_to_motorcycle(self, plate, date_, km, service_type, cost, notes=""):
        mc = self._user.get_motorcycle_by_plate(plate)
        if mc is None:
            raise ValueError(f"Motor dengan plat {plate} tidak ditemukan.")

        record = ServiceRecord(date_, km, service_type, cost, notes)
        mc.add_service(record)

    def get_service_history(self, plate):
        mc = self._user.get_motorcycle_by_plate(plate)
        if mc is None:
            return []
        return mc.service_records
    
    def remove_motorcycle(self, plate: str):
        removed = self._user.remove_motorcycle_by_plate(plate)
        if not removed:
            raise ValueError(f"Motor dengan plat {plate} tidak ditemukan.")
        
    def update_service_for_motorcycle(self, plate, index: int, date_, km, service_type, cost, notes=""):
        mc = self._user.get_motorcycle_by_plate(plate)
        if mc is None:
            raise ValueError(f"Motor dengan plat {plate} tidak ditemukan.")

        mc.update_service(index, date_, km, service_type, cost, notes)
