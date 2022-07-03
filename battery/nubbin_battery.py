from battery.battery import Battery
from utils import add_years_to_date

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date)
        self.threshold = 4
    
    def needs_service(self):
        service_threshold_date = add_years_to_date(
            self.last_service_date,
            self.threshold
        )
        return service_threshold_date < self.current_date
