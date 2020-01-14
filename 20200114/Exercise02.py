# https://github.com/BoxBy/Cpp/tree/master/20191114 : Cpp to Python

class Clock :
    def __init__(self, hour = 12, min = 0, apm = 0) :
        self.__hour = hour
        self.__min = min
        self.__apm = bool(apm)

    def tick(self, rep) :
        for i in range(rep) :
            self.__min += 1
            if min == 60 :
                self.__hour += 1
                self.__min = 0

            if self.__hour == 13 :
                self.__hour = 1

            if self.__hour == 12 and self.__min == 0 :
                self.__apm = not self.__apm
        
        return self

    def __add__(self, other) :
        return self.tick(other)

    def __str__(self) :
        ret = "{:0>2} : {:0>2}".format(self.__hour, self.__min)
        if self.__apm == True :
            ret += " PM"
        else :
            ret += " AM"
        return ret


c = Clock()
d = Clock()

print("Clock c = [{}]".format(c))
print("CLock d = [{}]".format(d))

c = d + 1

print("Clock c = [{}]".format(c))
print("CLock d = [{}]".format(d))