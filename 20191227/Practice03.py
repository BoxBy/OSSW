# https://github.com/BoxBy/Cpp/tree/master/20190926 : Cpp to Python

from operator import itemgetter


class proverb:
    def __init__(self, word, line):
        self.__word_count = word
        self.__line_count = line
        self.__pointer = 0
        self.__compare_count = 0
        self.__lines = [[' ', ], ]
        self.__compare = [0]
        self.__counts = [0]
        for i in range(self.__line_count): # using like static list
            self.__lines.append(' ')

    def getProverb(self, line, word):
        return self.__lines[line][word]
    
    def stringIn(self, string):
        string.strip(';')
        self.__lines[self.__pointer] = string.split()
        for i in range(len(self.__lines[self.__pointer])):
            self.compareCount(self.__pointer, i)
        self.__pointer += 1

    def compareCount(self, line, word): # count
        compareWord = self.__lines[line][word].lower()
        if compareWord in self.__compare :
            self.__counts[self.__compare.index(compareWord)] += 1
            self.__compare_count += 1
        else :
            self.__counts.append(1)
            self.__compare.append(compareWord)
        
    def bigFive(self):
        counts_compare = []
        print("Top 5 Words")
        for i in range(1, len(self.__compare)):
            counts_compare.append([self.__compare[i], self.__counts[i]])
            
        counts_compare.sort(reverse = True, key = itemgetter(1))

        for i in range(5):
            print("{} = {}".format(i + 1, counts_compare[i]))


Proverbs = proverb(50, 100)
try:
    inFile = open("test.txt", 'r')
    lines = inFile.readlines()
    for line in lines:
        Proverbs.stringIn(line)
except FileNotFoundError as e:
    print("Exception opening/reading file")

Proverbs.bigFive()