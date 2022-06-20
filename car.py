from abc import ABC, abstractmethod

from battery.battery import Battery
from engine.engine import Engine

class Car(ABC):
    def __init__(self, battery: Battery, engine: Engine):
        self.battery = battery
        self.engine = engine
        
    @abstractmethod
    def needs_service(self):
        pass
