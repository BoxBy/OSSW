# https://github.com/BoxBy/Cpp/tree/master/20191017 : Cpp to Python

class BC1 :
    def __init__(self):
        self.__x = 0

    def set_x(self, a) :
        self.__x = a

class BC2 :
    def __init__(self):
        self.__x = 0

    def set_x(self, a) :
        self.__x = a

class DC(BC1, BC2):
    def __init__(self):
        super(BC1, self).__x = 0
        super(BC2, self).__x = 0
        self.__x = 0

    def set_x(self, a):
        self.__x = a

def tester():
    d1 = DC()

    d1.set_x(137)

    d1.BC1.set_x(1.23) # ERROR

    d1.BC2().set_x('c') # ERROR

tester()

#ERROR