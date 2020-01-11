# https://github.com/BoxBy/Cpp/tree/master/20191031 : Cpp to Python

class TradesPerson :
    def sayHi(self):
        print("Just Hi")

class Tinker(TradesPerson) :
    def sayHi(self):
        print("Hi, I tinker")
    

class Tailor(TradesPerson) :
    def sayHi(self):
        print("Hi, I tailor")
    
while(True) :
    which = int(input("1 == TradesPerson, 2 == Tinker, 3 == Tailor"))
    if which >= 1 and which <= 3 :
        break

if which == 1 :
    p = TradesPerson()
elif which == 2 :
    p = Tinker()
else :
    p = Tailor()

p.sayHi()
del p
