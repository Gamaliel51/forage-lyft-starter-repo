from tire.tire import Tire


class OctoPrime(Tire):
    def __init__(self, tire_data_array):
        self.tire_data = tire_data_array

    def needs_service(self):
        array_sum = 0

        for i in self.tire_data:
            array_sum += i

        if array_sum >= 3:
            return True
        else:
            return False