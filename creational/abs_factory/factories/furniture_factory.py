import abc

from creational.abs_factory.furnitures.abs_chair import AbsChair
from creational.abs_factory.furnitures.abs_coffee_table import AbsCoffeeTable
from creational.abs_factory.furnitures.abs_sofa import AbsSofa


class AbsFurnitureFactory(abc.ABC):
    @abc.abstractmethod
    def create_chair(self) -> AbsChair:
        pass

    @abc.abstractmethod
    def create_sofa(self) -> AbsSofa:
        pass

    @abc.abstractmethod
    def create_coffee_table(self) -> AbsCoffeeTable:
        pass
