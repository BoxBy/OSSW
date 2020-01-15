# https://github.com/BoxBy/Cpp/tree/master/20191121 : Cpp to Python

# list

PUSH_FRONT = 1
PUSH_BACK = 2
POP_FRONT = 3
POP_BACK = 4
SIZE = 5
EMPTY = 6
FRONT = 7
BACK = 8

def switch_on(string) :
    if string[0:4] == "push" :
        if string[5:10] == "front" :
            return PUSH_FRONT
        else :
            return PUSH_BACK
    
    elif string[0:3] == "pop" :
        if string[4:9] == "front" :
            return POP_FRONT
        else :
            return POP_BACK

    elif string == "size" :
        return SIZE

    elif string == "empty" :
        return EMPTY

    elif string == "front" :
        return FRONT

    elif string == "back" :
        return BACK

    else :
        return 0

def pushNum(string, num) :
    if num == PUSH_FRONT :
        return int(string[11:])
    else:
        return int(string[10:])

deque = []

input_data = input("First push : ")
deque.append(int(input_data))

while True :
    input_data = input("Next Command : ")
    command = switch_on(input_data)
    if command == PUSH_FRONT or command == PUSH_BACK :
        input_data = input_data.split()
        num = int(input_data.pop())
    
    if command == PUSH_FRONT :
        deque.insert(deque[0], num)

    elif command == PUSH_BACK :
        deque.append(num)

    elif command == POP_FRONT :
        try :
            num = deque[0]
            del deque[0]
        except :
            num = -1

    elif command == POP_BACK :
        try :
            num = deque.pop()
        except :
            num = -1

    elif command == SIZE :
        num = len(deque)

    elif command == EMPTY :
        if len(deque) == 0 :
            num = True
        else:
            num = False
    
    elif command == FRONT :
        try :
            num = deque[0]
        except :
            num = -1

    elif command == BACK :
        try :
            num = deque[len(deque) - 1]
        except :
            num = -1
    else :
        break

    print(num)
    print(deque)