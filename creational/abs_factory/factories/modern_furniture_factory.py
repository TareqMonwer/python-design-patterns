from creational.abs_factory.factories.furniture_factory import AbsFurnitureFactory
from creational.abs_factory.furnitures.chair import ModernChair
from creational.abs_factory.furnitures.coffee_table import ModernCoffeeTable
from creational.abs_factory.furnitures.sofa import ModernSofa


class ModernFurnitureFactory(AbsFurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()

    def create_coffee_table(self):
        return ModernCoffeeTable()
