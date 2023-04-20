from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine


class Thovex(Car):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__()
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = None

    def needs_service(self):
        if self.engine.needs_service():
            return True
        else:
            return False
