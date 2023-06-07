from inspect import getmembers, isclass, isabstract

import factory


class AutoFactory:
    autos = {}    # Key: Car model name, Value: class for the Car

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(factory,
                             lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, factory.abs_autos.AbsAuto):
                self.autos.update([[name, _type]])

    def create_instance(self, car_name):
        if car_name in self.autos:
            return self.autos[car_name]()
        else:
            return factory.NullCar(car_name)
