# https://github.com/BoxBy/Cpp/tree/master/20191031 : Cpp to Python

class Base :
    def __init__(self) :
        self.__s = "Base"
        print("Base Class")

    def what(self) :
        print(self.__s)

class Derived(Base) :
    def __init__(self) :
        self.__s = "Derived"
        print("Derived Class")

    def what(self):
        print(self.__s)
    
p = Base()
c = Derived()

p.what()
c.what()

c = Base()
p = Derived()

p.what()
c.what()

del c
del p