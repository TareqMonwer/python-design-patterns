# Creational Pattern
from creational.factory_basic.cars.abs_autos import AbsAuto


class Chevy(AbsAuto):
    def start(self):
        print("Chevy is running...")

    def stop(self):
        print("Chevy is stopped.")
