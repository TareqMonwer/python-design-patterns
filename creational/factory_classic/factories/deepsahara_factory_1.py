from .abs_factory import AbsFactory
from factory_classic.autos import DeepSahara


class DeepSaharaFactory(AbsFactory):
    def create_auto(self):
        self.deepsahara = deepsahara = DeepSahara()
        deepsahara.name = "Deep Sahara"
        return deepsahara
