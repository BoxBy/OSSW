# https://github.com/BoxBy/Cpp/tree/master/20191107 : Cpp to Python


class Pair:
    def __init__(self, f1, f2) :
        self.p1 = f1
        self.p2 = f2
    
    def __eq__(self, other) :
        return ((self.p1 == other.p1) and (self.p2 == other.p2))

s1 = Pair(1, 2)
s2 = Pair(2, 1)

if s1 == s2 :
    print("Same")
else :
    print("Not Same")

s3 = Pair(1, 2)

if s1 == s3 :
    print("Same")
else :
    print("Not Same")
