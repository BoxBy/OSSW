# https://github.com/BoxBy/Cpp/tree/master/20191114 : Cpp to Python

class Frame :
    def __init__(self, name = "NoName") :
        self.__name = name
        self.print()
    
    def print(self) :
        print("{} created".format(self.__name))
    

a = []

names = ["f1", "f2", "f3", "f4"]

try :
    a.append(Frame())
    # the 1st Frame with NoNames

    for i in range(4) :
        a.append(Frame(names[i]))
    
except Exception as s :
    print(s)
    quit()
