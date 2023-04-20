from datetime import datetime
from car import Car
from engine.sternman_engine import SternmanEngine


class Palindrome(Car):
    def __init__(self, warning_light_is_on):
        super().__init__()
        self.engine = SternmanEngine(warning_light_is_on)
        self.battery = None

    def needs_service(self):
        if self.engine.needs_service():
            return True
        else:
            return False
