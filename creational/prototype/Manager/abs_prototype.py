import abc


class AbsPrototype(object):
    @abc.abstractmethod
    def clone(self):
        pass