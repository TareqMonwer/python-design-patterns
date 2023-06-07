from creational.abs_factory.factories.furniture_factory import AbsFurnitureFactory
from creational.abs_factory.furnitures.chair import VictorianChair
from creational.abs_factory.furnitures.coffee_table import VictorianCoffeeTable
from creational.abs_factory.furnitures.sofa import VictorianSofa


class VictorianFurnitureFactory(AbsFurnitureFactory):
    def create_chair(self):
        print(f"{self.__name__} Created...")
        return VictorianChair()

    def create_sofa(self):
        print(f"{self.__name__} Created...")
        return VictorianSofa()

    def create_coffee_table(self):
        print(f"{self.__name__} Created...")
        return VictorianCoffeeTable()
