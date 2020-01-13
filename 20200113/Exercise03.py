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

    def __mul__(self, other) :
        return Complex(self.getReal() * other.getReal() - self.getImag() - other.getImag(), self.getReal() * other.getImag() - self.getImag() * other.getReal())

    def __truediv__(self, other) :
        return Complex((self.getReal() * other.getReal() + self.getImag() * other.getImag()) / (other.getReal() * other.getReal() + other.getImag() * other.getImag()), (self.getImag() * other.getReal() - self.getReal() * other.getImag()) / (other.getReal() * other.getReal() + other.getImag() * other.getImag()))

    def print(self) :
        print("real : {}, imag : {}".format(self.__real, self.__imag))


a = Complex(0)
b = Complex(4.3, -8.2)
c = Complex(1.1, 2.3)

a = b + 5.1
a.print()
a = 5.1 + b
a.print()
a = b - 1.1
a.print()
a = b * c
a.print()
a = b / c
a.print()
