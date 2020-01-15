# https://github.com/BoxBy/Cpp/tree/master/20190919 : Cpp to Python

# File Out

fOut = open("Info.txt", 'w')

print("The number of team members : ")
teamNum = int(input()) #python input is string

if fOut.writable():
    print("Name", "{: >10}".format("Age"), "{: >22}".format("Phone"))
    for i in range(teamNum, 0, -1):
        print("Name : ", end = '')
        name = input()
        print("Age : ", end = '')
        age = input()
        print("phoneNumber : ", end = '')
        phoneNum = input()
        print()
        fOut.write(name)
        fOut.write("{: >10}".format(age))
        fOut.write("{: >22}".format(phoneNum))

fOut.close()