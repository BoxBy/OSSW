# https://github.com/BoxBy/Cpp/tree/master/20191128 : Cpp to Python

class Wordlist :
    def __init__(self) :
        self.__dictonary = []
        self.__wordlist = []

        inFile = open("dict.txt", 'r')
        lines = inFile.readlines()

        for line in lines :
            self.__dictonary.append(line)

        inFile.close()
    
    def CheckDictionary(self, string) :
        if string in self.__dictonary :
            return
    
        raise str("Not exist word in dictionary")
    
    def CheckDuplication(self, string) :
        if string in self.__wordlist :
            raise str("It's Duplication")
            
    def CheckConfirm(self, string) :
        if len(self.__wordlist) == 0 :
            return
        if self.__wordlist[-1][-1] != string[0] :
            raise str("Not same as the previous word alphabet")

    def add(self, string) :
        outFile = open("result.txt", 'w')
        try :
            self.CheckDictionary(string)
            self.CheckDuplication(string)
            self.CheckConfirm(string)
        except Exception as reason:
            print("You Lose. ", end = '')
            outFile.close()
            raise reason
        
        self.__wordlist.append(string)
        print(self.__wordlist)

        outFile.write(string, " ")

    def startGame(self) :
        print("Game Start")
        try :
            while True :
                word = input("Input Word : ")
                try :
                    word.upper()
                except :
                    raise str("It is not English")
            self.add(word)
        
        except Exception as reason :
            print(reason)

wl = Wordlist()
wl.startGame()