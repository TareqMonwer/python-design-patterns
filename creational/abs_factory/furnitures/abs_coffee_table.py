import abc


class AbsCoffeeTable(abc.ABC):
    @abc.abstractmethod
    def get_color(self):
        pass
