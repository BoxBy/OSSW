# https://github.com/BoxBy/Cpp/tree/master/20190919 : Cpp to Python

fIn = open("calculation.txt", 'r')

strings = fIn.readlines()
for string in strings:
    isHex = False
    if string[0] == '0':
        isHex = True
    string = string.split(' ')
#    print("string1 : ", string[0])
#    print("string2 : ", string[1])
#    print("string3 : ", string[2])

    if isHex == True:
        string[0] = int(string[0], 16)
        string[2] = int(string[2], 16)
    else:
        string[0] = int(string[0])
        string[2] = int(string[2])
    
    if isHex == True:
        print("{: <6}".format(hex(string[0])), "{: >2}".format(string[1]), "{: >6}".format(hex(string[2])), " = ", end = '')

        if string[1] == '+':
            print("{: >4}".format(hex(string[0] + string[2])))
        elif string[1] == '-':
            print("{: >4}".format(hex(string[0] - string[2])))
        elif string[1] == '/':
            print("{: >4}".format(hex(string[0] + string[2])))
    
    else:
        print("{: <6}".format(string[0]), "{: >2}".format(string[1]), "{: >6}".format(string[2]), " = ", end = '')

        if string[1] == '+':
            print("{: >4}".format(string[0] + string[2]))
        elif string[1] == '-':
            print("{: >4}".format(string[0] - string[2]))
        elif string[1] == '/':
            print("{: >4}".format(string[0] + string[2]))
        elif string[1] == '*':
            print("{: >4}".format(string[0] * string[2]))

fIn.close()



