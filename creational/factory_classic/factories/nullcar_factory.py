from .abs_factory import AbsFactory
from creational.factory_classic.autos import NullCar


class NullCarFactory(AbsFactory):
    def create_auto(self):
        self.nullcar = nullcar = NullCar("(Unknown)")
        nullcar.name = "(Unknown)"
        return nullcar
