
from battery.battery import Battery
from engine.engine import Engine

class Car:
    def __init__(self, battery: Battery, engine: Engine):
        self.battery = battery
        self.engine = engine
        
    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
