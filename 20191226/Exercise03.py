inFile = open("input.txt", 'r')
oFile = open("input.txt", 'w')

if not(inFile.readable()) :
    print("Can not find file")
    quit()

lines = inFile.readlines()
for line in lines:
    print(line)

### SAME OUTPUT ###
#while True:
#    line = inFile.readline()
#    if not line :
#        break
#    print(line)

inFile.close()


#if oFile.readable():
#    string = input()
#    oFile.write(string)
#oFile.close()

re_inFile = open("input.txt", 'r')
lines = re_inFile.readlines()
for line in lines:
    print(line)
re_inFile.close()