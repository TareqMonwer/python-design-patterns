class Borg:
    state = {}

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__dict__ = self.state
        return self


