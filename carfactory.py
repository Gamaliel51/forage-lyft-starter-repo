from car import Car

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import Spindler
from battery.nubbin_battery import Nubbin


class CarFactory(Car):

    @staticmethod
    def create_calliope(today, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(today, last_service_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_glissade(today, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(today, last_service_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_palindrome(today, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = Spindler(today, last_service_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_rorschach(today, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(today, last_service_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_thovex(today, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(today, last_service_date)
        car = Car(engine, battery)

        return car

