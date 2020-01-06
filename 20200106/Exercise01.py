# https://github.com/BoxBy/Cpp/tree/master/20191010 : Cpp to Python

class Person:
    def __init__(self):
        self.__age = 0
    def setAge(self, n):
        self.__age = n
    def getAge(self):
        return self.__age

p1 = Person()
p1.setAge(11)
print(p1.getAge())
p2 = p1
print(p2.getAge())
#python do not have pointer
#print(p3->getAge())
