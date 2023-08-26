class Singleton(object):
    ans = None

    @staticmethod
    def instance():
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton() # type: ignore
        return Singleton._instance # type: ignore


s1 = Singleton.instance()
s2 = Singleton.instance()

assert s1 is s2

s1.ans = 50 # type: ignore

assert s1.ans == s2.ans
print("Assertions passed.")