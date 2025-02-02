from abc import ABC, abstractmethod
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self):
        self.engine = None
        self.battery = None

    @abstractmethod
    def needs_service(self):
        pass
