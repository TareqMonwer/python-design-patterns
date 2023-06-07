# Creational Pattern
from creational.factory_basic.cars.abs_autos import AbsAuto


class NullCar(AbsAuto):
    def __init__(self, carname):
        self.carname = carname

    def start(self):
        print(f"(Unknown) {self.carname} is running...")

    def stop(self):
        print(f"(Unknown) {self.carname} is stopped.")
