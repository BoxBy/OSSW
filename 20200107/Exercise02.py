# https://github.com/BoxBy/Cpp/tree/master/20191017 : Cpp to Python

class Animal:
    def __init__(self, string = None):
        if string is None : # constructor overloading
            self.__species = "Animal"
        else:
            self.__species = string

class Primate(Animal):
    def __init__(self, n = None):
        Animal("Primate")
        if n is None :
            self.__heart_cham = n
        else :
            self.__heart_cham = 0

    
slug = Animal()
tweety = Animal("canary")
godzilla = Primate()
human = Primate(4)