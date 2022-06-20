from datetime import datetime

from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super(current_date, last_service_date).__init__()
        self.threshold = 4
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year = self.last_service_date.year + self.threshold
        )
        return service_threshold_date < self.current_date
