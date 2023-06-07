from abs_factory.furnitures.abs_chair import AbsChair


class ArtDecoChair(AbsChair):
    def has_legs(self):
        print(f"{self.__class__.__name__} has 4 legs")

    def seat_on(self):
        print(f"{self.__class__.__name__} has seat")


class VictorianChair(AbsChair):
    def has_legs(self):
        print(f"{self.__class__.__name__} has 4 stylish legs")

    def seat_on(self):
        print(f"{self.__class__.__name__} has larger seat")


class ModernChair(AbsChair):
    def has_legs(self):
        print(f"{self.__class__.__name__} has 2 minimal legs")

    def seat_on(self):
        print(f"{self.__class__.__name__} has a small minimal seat")
