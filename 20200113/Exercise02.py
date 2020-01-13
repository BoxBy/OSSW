# https://github.com/BoxBy/Cpp/tree/master/20191107 : Cpp to Python

class Complex :
    def __init__(self, r, i = None) :
        self.__real = r
        if i is None :
            self.__imag = 0
        else :
            self.__imag = i

    def getReal(self) :
        return self.__real
    
    def getImag(self) :
        return self.__imag

    def __add__(self, other) :
        return Complex(self.getReal() + other.getReal(), self.getImag() + other.getImag())
    
    def __sub__(self, other) :
        return Complex(self.getReal() - other.getReal(), self.getImag() - other.getImag())

    def print(self) :
        print("real : {}, imag : {}".format(self.__real, self.__imag))


c1 = Complex(0)
c2 = Complex(1.0, 2.0)
c3 = Complex(2.0, 3.0)

c1 = c2 + c3
c1.print()

c1 = c3 - c2
c1.print()
    
