# Creational Pattern
from .abs_autos import AbsAuto


class NullCar(AbsAuto):
    def __init__(self, carname):
        self.carname = carname

    def start(self):
        print(f"{self.carname} is running...")

    def stop(self):
        print(f"{self.carname} is stopped.")
