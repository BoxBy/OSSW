# https://github.com/BoxBy/Cpp/tree/master/20190926 : Cpp to Python

import random

class underFlow(Exception):
    pass
class overFlow(Exception):
    pass

MaxSize = 1000
arr = [random.randrange(0, 1000), ]
for i in range(MaxSize + 1):
    arr.append(random.randrange(0, 1000))

def access(i):
    if i < 0 :
        raise underFlow
    elif i >= MaxSize :
        raise overFlow
    return arr[i]


def g(i):
    try:
        val = access(i)
    except underFlow:
        print("arr : underFlow....aborting")
        quit()
    except overFlow:
        print("arr : overFlow....aborting")
        quit()
    print("arr[{}] = {}".format(i, val))


g(int(input()))
