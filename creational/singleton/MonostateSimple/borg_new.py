class Borg:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        self = super(Borg, cls).__new__(cls, *args, **kwargs)
        self.__dict__ = cls.__shared_state
        return self


if __name__ == "__main__":
    b = Borg()
    b2 = Borg()
    b.name = "Honda"

    print(b.__dict__)
    print(b2.__dict__)

