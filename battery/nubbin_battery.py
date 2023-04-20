from battery.battery import Battery
from datetime import date
from dateutil import relativedelta


class Nubbin(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        today = date.today()
        last_service_date = self.last_service_date

        date_difference = relativedelta.relativedelta(today, last_service_date)
        if date_difference.years >= 4:
            return True
        else:
            return False
