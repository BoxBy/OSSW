# https://github.com/BoxBy/Cpp/tree/master/20191128 : Cpp to Python

def __print(begin, end) : 
    while begin != end :
        print(f"[{begin}]", end = '')
        begin += 1
    print()

class is_odd :
    def __init__(self) :
        self.__num_delete = 0
        self.__list = []

    def __call__(self, i) :
        if self.__num_delete >= 2 :
            return False
        
        if i % 2 == 1 :
            self.__num_delete += 1
            return True

        return False

    def remove_if(self) :
        for lst in self.__list :
            if self.__call__(lst) :
                self.__list.remove(lst)

    def push_back(self, num) :
        self.__list.append(num)

    def getlist(self) :
        return self.__list

vec = is_odd()

vec.push_back(5)
vec.push_back(3)
vec.push_back(1)
vec.push_back(2)
vec.push_back(3)
vec.push_back(4)


print("Original List : {}".format(vec.getlist()))

print("Erase 2 odd elements")
vec.remove_if()
print(vec.getlist())

