from abs_factory.furnitures.abs_sofa import AbsSofa


class ArtDecoSofa(AbsSofa):
    def sit(self):
        print(f"You can sit on {self.__name__}")

    def sleep(self):
        print(f"You can't sleep on {self.__name__}")


class VictorianSofa(AbsSofa):
    def sit(self):
        print(f"You can sit on {self.__name__}")

    def sleep(self):
        print(f"You can sleep on {self.__name__}")


class ModernSofa(AbsSofa):
    def sit(self):
        print(f"You can sit on {self.__name__}")

    def sleep(self):
        print(f"You can't sleep on {self.__name__}")
