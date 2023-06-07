from .abs_factory import AbsFactory
from factory_classic.autos import Honda


class HondaFactory(AbsFactory):
    def create_auto(self):
        self.honda = honda = Honda()
        honda.name = "Honda"
        return honda
