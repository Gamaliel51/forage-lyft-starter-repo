from tire.tire import Tire


class Carrigan(Tire):
    def __init__(self, tire_data_array):
        self.tire_data = tire_data_array

    def needs_service(self):
        for i in self.tire_data:
            if i >= 0.9:
                return True
        return False
