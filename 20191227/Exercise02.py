# https://github.com/BoxBy/Cpp/tree/master/20190926 : Cpp to Python

vals = [10.2, 12.6, 33.1, 24.1, 50.0] # list

def setValues(i, data):
    global vals
    vals[i] = data

def swap(a, b):
    a, b = b, a

i = 7
j = 3
print("Call by assignment")
print("i = {}".format(i))
print("j = {}".format(j))
swap(i, j) # send immutable object(int, float, str, tuple, etc...)
print("i = {}".format(i))
print("j = {}".format(j))
print()

print("Call by reference")
print("Value before change")
for k in range(4):
    print("vals[{}] = ".format(k), vals[k])

setValues(1, 20.23) # send mutable object(ex: list, dict, set, etc...)
setValues(3, 70.8)
print("Value after change")
for k in range(4):
    print("vals[{}] = ".format(k), vals[k])
