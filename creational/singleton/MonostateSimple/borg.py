class Borg:
    __shared_state = {}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


if __name__ == "__main__":
    b = Borg()
    b2 = Borg()
    b.x = 10

    print("Borg b", b.__dict__)
    print("Borg b2", b2.__dict__)

