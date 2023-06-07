# Creational Pattern
from .abs_autos import AbsAuto


class DeepSahara(AbsAuto):
    def start(self):
        print("DeepSahara is running...")

    def stop(self):
        print("DeepSahara is stopped.")
