from creational.abs_factory.furnitures.abs_coffee_table import AbsCoffeeTable


class ArtDecoCoffeeTable(AbsCoffeeTable):
    def get_color(self):
        print(f"{self.__class__.__name__} is Red")


class VictorianCoffeeTable(AbsCoffeeTable):
    def get_color(self):
        print(f"{self.__class__.__name__} is Dark")


class ModernCoffeeTable(AbsCoffeeTable):
    def get_color(self):
        print(f"{self.__class__.__name__} is Off-white")
