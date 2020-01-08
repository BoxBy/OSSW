# https://github.com/BoxBy/Cpp/tree/master/20191024(Mid-Exam) : Cpp to Python

# Mixing Problem01, Problem92
# Problem01 has one value
# Problem02 has two value using '//'


class Entry:
    def __init__(self, key = None, value = None) :
        self.__key = 0
        if key is not None :
            self.__key = key
            self.__value = value
    
    def setKey(self, key) :
        self.__key = key

    def setValue(self, value) :
        self.__value = value
    
    def getKey(self) :
        return self.__key
    
    def getValue(self) :
        return self.__value

class Dictonary:
    def __init__(self) :
        self.__entries = [Entry()]
    
    def find(self, key) :
        try:
            for find in self.__entries :
                if find.getKey() == key :
                    return self.__entries.index(find)
        except Exception :
            print("FINDING ERROR: Key Not Found")
            return None

    def insert(self, key, value) :
        if self.find(key) == None :
            self.__entries.append(Entry(key, value))
        else :
            print("INSERT ERROR: Already Exist")
    
    def modify(self, key, value) :
        try :
            self.__entries[self.__entries.index(self.find(key))].setValue(value)
        except Exception :
            print("MODIFY ERROR: Key Not Found")

    def deletion(self, key) :
        try:
            location = self.__entries.index(self.find(key))
            ret = self.__entries[location].getValue()
            del self.__entries[location]
            del location
            return ret
        except Exception :
            print("DELETION ERROR: Key Not Found")
            return None

    def addValue(self, key, value) :
        try:
            location = self.find(key)
            value_temp = self.__entries[location].getValue()
            value_temp = value_temp + '//' + value
            self.__entries[location].setValue(value_temp)
            del location
            del value_temp
        except Exception :
            print("ADD ERROR: Key Not Found")

inFile = open("dictonary.txt", 'r')
#inFile = open("dictonary2.txt", 'r')
lines = inFile.readlines()
d = Dictonary()

for line in lines :
    print(line)
    line.split(':')
    print(line[0], line[1])
    d.insert(line[0], line[1])

inFile.close()

print("Find key 'Apple'")
print(d.find("Apple"))
choose = int(input("1. Modify 'Apple' meaning and 2. find again key 'Apple' : "))

if choose == 1 :
    modify = input("Input : ")
    d.modify("Apple", modify)
    del modify
elif choose == 2 :
    print(d.find("Apple"))

print("Find Key 'Orange'")
print(d.find("Orange"))

choose = int(input("1. Delete 'Orange' and 2. Find again key 'Orange'"))

if choose == 1 :
    d.deletion("Orange")
elif choose == 2 :
    print(d.find("Orange"))

del d
del choose