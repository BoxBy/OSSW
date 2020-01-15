# https://github.com/BoxBy/Cpp/tree/master/20190919 : Cpp to Python

i = 0

def f1():
#    i += 1 #ERROR
    i  = 0
    i += 1 # python doesn't using ++/--

i = 0
f1()
print("Global variable i : ", i(globals))
print("i : ", i)

# do not use return