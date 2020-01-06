# https://github.com/BoxBy/Cpp/tree/master/20191010 : Cpp to Python

class Namelist:
    def __init__(self, string, i):
        self.__p = []
        self.__size = i
        for i in range(self.__size):
            self.__p.append(string[i])

    def _set(self, s, i): # already have set
        self.__p[i] = s
    
    def dump(self):
        for i in range(self.__size):
            print(self.__p[i])
        
stringList = ["Lab", "Husky", "Collie"]
d1 = Namelist(stringList, 3)
d2 = Namelist(stringList, 3)
d1.dump()
d2._set("Great Dane", 1)
d2.dump()
d1.dump()

