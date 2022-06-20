from car import Car
from battery import NubbinBattery, SpindlerBattery
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine

def create_calliope(
    current_date, last_service_date, current_mileage, last_service_mileage
):
    battery = SpindlerBattery(current_date, last_service_date)
    engine = CapuletEngine(
        last_service_date, current_mileage, last_service_mileage
    )
    return Car(battery, engine)

def create_glissade(
    current_date, last_service_date, current_mileage, last_service_mileage
):
    battery = SpindlerBattery(current_date, last_service_date)
    engine = WilloughbyEngine(
        last_service_date, current_mileage, last_service_mileage
    )
    return Car(battery, engine)

def create_palindrome(current_date, last_service_date, warning_light_on):
    battery = SpindlerBattery(current_date, last_service_date)
    engine = SternmanEngine(warning_light_on)
    return Car(battery, engine)

def create_rorschach(
    current_date, last_service_date, current_mileage, last_service_mileage
):
    battery = NubbinBattery(current_date, last_service_date)
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    return Car(battery, engine)

def create_thovex(
    current_date, last_service_date, current_mileage, last_service_mileage
):
    battery = NubbinBattery(current_date, last_service_date)
    engine = CapuletEngine(
        last_service_date, current_mileage, last_service_mileage
    )
    return Car(battery, engine)