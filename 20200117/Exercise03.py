# https://github.com/BoxBy/Cpp/tree/master/20191128 : Cpp to Python

def showWidth() :
    print("{: >19}".format("Hello"))
    print("{: >5}{}{: >10}Korea/Seoul/City".format(12, '%', 10))

showWidth()
print()

print("{:-}", end = '')
showWidth()
print()