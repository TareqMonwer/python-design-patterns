# Creational Pattern
from creational.factory_basic.cars.abs_autos import AbsAuto


class Honda(AbsAuto):
    def start(self):
        print("Honda is running...")

    def stop(self):
        print("Honda is stopped.")
