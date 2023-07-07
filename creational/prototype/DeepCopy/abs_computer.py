import abc


class AbsComputer(object):
    @abc.abstractmethod
    def display(self):
        pass
