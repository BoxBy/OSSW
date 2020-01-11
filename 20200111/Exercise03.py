# https://github.com/BoxBy/Cpp/tree/master/20191031 : Cpp to Python

class First:
    def __init__(self, string) :
        self.__strOne = string

    def __del__(self) :
        print("__del__ First()")
        del self.__strOne

class Second(First) :
    def __init__(self, string1, string2) :
        super().__init__(string1)
        self.__strTwo = string2
    
    def __del__(self) :
        print("__del__ Second")
        del self.__strTwo
    
ptr = Second("Simple", "Complex")
del ptr
