# Creational Pattern
from creational.factory_basic.cars.abs_autos import AbsAuto


class DeepSahara(AbsAuto):
    def start(self):
        print("DeepSahara is running...")

    def stop(self):
        print("DeepSahara is stopped.")
