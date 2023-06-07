from abs_factory.factories.furniture_factory import AbsFurnitureFactory


class VictorianFurnitureFactory(AbsFurnitureFactory):
    def create_chair(self):
        print(f"{self.__name__} Created...")

    def create_sofa(self):
        print(f"{self.__name__} Created...")

    def create_coffee_table(self):
        print(f"{self.__name__} Created...")
