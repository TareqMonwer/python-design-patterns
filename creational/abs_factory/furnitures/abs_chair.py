import abc


class AbsChair(abc.ABC):
    @abc.abstractmethod
    def has_legs(self):
        pass

    @abc.abstractmethod
    def seat_on(self):
        pass
