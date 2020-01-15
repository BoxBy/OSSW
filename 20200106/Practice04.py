# https://github.com/BoxBy/Cpp/tree/master/20191010 : Cpp to Python

# String implement
class MyString:
    def __init__(self, string):
        self.__string_length = len(string)
        self.__string_content = string

    def setString(self, string):
        self.__string_length = len(string)
        self.__string_content = string
    
    def getMyString(self):
        temp = MyString(self.__string_content)
        return temp

    def getString(self):
        return self.__string_content

    def length(self):
        return self.__string_length

    def println(self):
        print(self.__string_content)

    def at(self, i):
        return self.__string_content[i]

    def insert(self, loc, string):
        temp = self.__string_content[:loc]
        temp += string
        temp += self.__string_content[loc:]
        self.__string_content = temp
        self.__string_length = len(temp)

    def find(self, find_from, string):
        length = len(string)
        for i in range(find_from, self.__string_length):
            if self.__string_content[i:i+length] == string :
                return i

        return -1

    def erase(self, loc, num):
        temp = self.__string_content[:loc]
        temp += self.__string_content[loc+num:]
        self.__string_content = temp
        self.__string_length = len(temp)


str1 = MyString("I love this long long string")
str2 = MyString("<some string inserted between>")
#str3 = MyString(str1)
str3 = MyString("I love this long long string")

#str1.reserve(30) # python didn't need reserving

print("str1")
#print("Capacity = {}".format(str1.capacity()))
print("String length = {}".format(str1.length()))
print("5th charactor = {}".format(str1.at(5)))
str1.println()
print()

print("str2")
print("str2")
#print("Capacity = {}".format(str2.capacity()))
print("String length = {}".format(str2.length()))
print("5th charactor = {}".format(str2.at(5)))
str2.println()
print()

str1.insert(5, "<some string inserted between>")
str1.erase(0, 3)
print("after insertion and erasure")
#print("Capacity = {}".format(str1.capacity()))
print("String length = {}".format(str1.length()))
str1.println()
print()

print("copy constructor str3")
#print("Capacity = {}".format(str3.capacity()))
print("String length = {}".format(str3.length()))
str3.println()
print()

str4 = MyString("")
str4.setString("this is a very very long string")
str4.println()
print()
print("find a word in str4")
print("find 1th <very> in the str4 = {}".format(str4.find(0, "very")))
print("find 2th <very> in the str4 = {}".format(str4.find(str4.find(0, "very") + 1, "very")))
