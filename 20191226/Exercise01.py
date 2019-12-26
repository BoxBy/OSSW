i = 0

def f1():
    i+=1 # python doesn't using ++/--
    i = 0
    i+=1

i = 0
f1()
print("Global variable i : ", i(globals))
print("i : ", i)

# do not use return