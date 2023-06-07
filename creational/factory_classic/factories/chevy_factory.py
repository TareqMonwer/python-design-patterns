from .abs_factory import AbsFactory
from factory_classic.autos import Chevy


class ChevyFactory(AbsFactory):
    def create_auto(self):
        self.chevy = chevy = Chevy()
        chevy.name = "Chevy Volt"
        return chevy
