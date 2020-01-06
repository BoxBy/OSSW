# https://github.com/BoxBy/Cpp/tree/master/20191010 : Cpp to Python

class C:
    def __init__(self):
        self.__num = 0
    def set(self, n):
        self.__num = n
    def get(self):
        return self.__num

def f(C):
    C.set(-999)

def g():
    c = C()
    c.set(123)
    return c

c1 = C()
c2 = C()
f(c1)
print(c1.get())
c2 = g()
print(c2.get())
