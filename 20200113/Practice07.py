# https://github.com/BoxBy/Cpp/tree/master/20191107 : Cpp to Python

def __truediv__(s1, s2) :
    count = 0
    for i in range(s1.size()) :
        if not s1.find(s2, i) == -1 :
            i = s1.find(s2, i)
            count += 1

    return count

def __sub__(s1, s2) :
    count = s1.find(s2)
    s1.erase(count, s2.size())
    return s1

def __mul__(s1, i) :
    temp = ''
    for j in range(i) :
        temp += s1
    return temp
    
# Operator Overloading only in Class

s1 = "this is test string, test is ok."

n = s1 / "test"
print(n)
s2 = s1 - "test"
print(s2)
s3 = s2 - "test"
print(s3)
n = s3 / "test"
print(n)
word1 = "test"
s4 = word1 * 3
print(s4)
s5 = s1 - "test" - "this"
print(s5)
word2 = "bbaq"
s6 = word2 * 3 * 2
print(s6)

del n
del s1
del s2
del s3
del s4
del s5
del s6
del word1
del word2