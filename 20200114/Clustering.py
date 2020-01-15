# https://github.com/BoxBy/Cpp/tree/master/K-mean/Clustering/Clustering : Cpp to Python
import random

class Kmeans :
    def __init__(self, cluster) :
        self.__word = [] # 4423, wordDict-dicTitle.txt
        self.__dict = [] # 500, wordDict-dicTitle.txt
        self.__array = [] # 4423 * 500, termDicMatrix.txt
        self.__group = [] # 500
        self.__K = cluster # clustering Value
        self.__Kvalue = [] # 4423 * K
        self.__J = 0

        for i in range(4423) :
            self.__array.append([])
            self.__word.append(0)

            for j in range(500) :
                self.__array[i].append(0)

        for j in range(self.__K) :
            self.__Kvalue.append([])
            for i in range(4423) :
                self.__Kvalue[j].append(0)

        for i in range(500) :
            self.__group.append(0)

    def resetK(self) :
        for k in range(self.__K) :
            j = random.randint(0, 500)
            for i in range(4423) :
                self.__Kvalue[k][i] = self.__array[i][j]
                
        self.__group = []
        for i in range(500) :
            self.__group.append(0)

    def setK(self) :
        count = [] # K
        temp = [[], ] # K * 4423

        for i in range(self.__K) :
            count.append(0)
            temp.append([])
            for j in range(4423) :
                temp[i].append(0)
        
        for j in range(500) :
            for k in range(self.__K) :
                if self.__group[j] == k :
                    self.groupSum(temp[k], self.__array, j)
                    count[k] += 1
            if j % 100 == 0 :
                print(".", end = '')

    def setArray(self, Matrix) :
        print("including termDicMatrix.txt")
        lines = Matrix.readlines()

        for line in lines :
            line = line.split()
            self.__array.append(line)
        
        print("Complete")

    def setValue(self, Dict) :
        print("including wordDict-docTitle.txt")

        for line in Dict[1:4424] :
            self.__word.append(self.clear(line))

        for line in Dict[4428:4927] :
            self.__dict.append(self.clear(line))
        
        print("Complete")

    def setJ(self) :
        print("Setting K")
        self.setK()
        print("Complete")
        print("Setting J")

        temp = 0

        for j in range(500) :
            for k in range(self.__K) :
                temp += self.groupMulSum(self.__array, j, int(self.__group[j]))
        
        self.__J = temp / 500
        print("Complete")

    def getJ(self) :
        return self.__J

    def clustering(self) :
        print("Clustering start")

        name = []
         
        for i in range(self.__K) :
            name.append([[1, -1], [1, -1], [1, -1], [1, -1], [1, -1]])
        
        temp = 1
        dicttemp = 1
        ktemp = 0

        for j in range(500) :
            temp = 1
            for k in range(self.__K) :
                if self.distance(self.__Kvalue[k], self.__array, j) < temp or k == 0 :
                    temp = self.distance(self.__Kvalue[k], self.__array, j)
                    ktemp = k
            
            self.__group[j] = ktemp
            dicttemp = j

            for l in range(5) :
                if name[ktemp][l][0] > temp :
                    dicttemp, name[ktemp][l][1] = name[ktemp][l][1], dicttemp
                    temp, name[ktemp][l][0] = name[ktemp][l][0], temp

        print("Complete")

        self.setJ()

        print("Top 5 Dicts")
        for i in range(5) :
            for j in range(self.__K) :
                if int(name[j][i][1]) == -1 :
                    print("{: >30}".format(''))
                else :
                    print("{: >30}".format(name[j][i][0]))
            print()

            for j in range(self.__K) :
                if int(name[j][i][1]) == -1 :
                    print("{: >30}".format(''))
                else:
                    print("{: >30}".format(self.__dict[int(name[j][i][1])]))
            print()

        del name
        del temp
        del ktemp
        del dicttemp

    def getK(self) :
        return self.__K

    def run(self, result) :
        i = 0
        for i in range(10) :
            self.resetK()
            result.append([])
            for j in range(20) :
                print()
                print()
                print("{}th Clustering".format(j + 1))
                result[i].append(self.clustering())

    
    def clear(self, Dict) : # delete "
        return Dict.strip('"')

    def distance(self, k, dest, i) :
        temp = 0
        for j in range(4423) :
            temp += pow(k[j] - dest[j][i], 2)

        return temp

    def groupSum(self, k, value, i) :
        for j in range(4423) :
            k[j] += value[j][i]

        return k

    def groupMulSum(self, value, i, k) :
        temp = 0
        for j in range(4423) :
            temp += pow(value[j][i] - self.__Kvalue[k][j], 2)

        return temp

result = []

for count in range(3) :
    temp = int(input("1. Random or 2. Select? : "))
    if temp == 1 :
        temp = random.randint(9, 20)
    elif temp == 2 :
        temp = input("K(9 ~ 20) : ")
    
    K = Kmeans(temp)
    print("K : {}".format(temp))
    
    Matrix = open("termDocMatrix.txt", 'r')
    K.setArray(Matrix)
    Matrix.close()

    Dict = open("wordDict-docTitle.txt", 'r')
    K.setValue(Dict)
    Dict.close()

    K.run(result)

    print("     1번     ｜     2번     ｜     3번     ｜     4번     ｜     5번     ｜     6번     ｜     7번     ｜     8번     ｜     9번     ｜     10번     ｜")
    for i in range(20) :
        for j in range(10) :
            print("{: >14}".format(result[j][i]), end = '')
        print()

del result
del temp


