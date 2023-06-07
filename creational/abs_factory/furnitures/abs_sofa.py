from abc import ABC, abstractmethod


class AbsSofa(ABC):
    """Abstract class representing a sofa."""
    @abstractmethod
    def sit(self):
        """Abstract method representing sitting on the sofa."""
        pass

    @abstractmethod
    def sleep(self):
        """Abstract method representing sleeping on the sofa."""
        pass
