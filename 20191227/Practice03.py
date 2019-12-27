# https://github.com/BoxBy/Cpp/tree/master/20190926 : Cpp to Python

#not complete
from operator import itemgetter


class proverb:
    def __init__(self, word, line):
        self.__word_count = word
        self.__line_count = line
        self.__pointer = 0
        self.__compare_count = 0
        self.__lines = [[' ', ], ]
        self.__counts = [[0, 0], ]
        for i in range(self.__line_count): # using like static list
            self.__lines.append(' ')

    def getProverb(self, line, word):
        return self.__lines[line][word]
    
    def stringIn(self, string):
        string.strip(';')
        self.__lines[self.__pointer] = string.split(' ')
        for i in range(len(self.__lines[self.__pointer])):
            self.compareCount(self.__pointer, i)
        self.__pointer += 1


    def compareCount(self, line, word): # count
        if self.__counts[0][0] == 0:
            self.__counts[0][0] = self.__lines[line][word]
            self.__counts[0][1] = 1
            self.__compare_count += 1
        else:
            for i in range(self.__compare_count):
                print("{}, {}".format(self.__counts[i][0], self.__lines[line][word]))
                if self.__counts[i][0] == self.__lines[line][word]:
                        self.__counts[i][1] += 1
                        self.__compare_count += 1
            
            self.__counts.append([self.__lines[line][word], 1])
        

        
    def bigFive(self):
#        self.__counts.sort(key = itemgetter(1))

#        for i in range(5):
        for temp in self.__counts:
            print(temp)           


Proverbs = proverb(50, 100)
try:
    inFile = open("test.txt", 'r')
    lines = inFile.readlines()
    for line in lines:
        Proverbs.stringIn(line)
except FileNotFoundError as e:
    print("Exception opening/reading file")

Proverbs.bigFive()