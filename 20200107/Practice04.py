# https://github.com/BoxBy/Cpp/tree/master/20191017 : Cpp to Python

NAME_LEN = 20
MAKE = int(1)
DEPOPSIT = int(2)
WITHDRAW = int(3)
INQUIRE = int(4)
EXIT = int(5)

LEVEL_A = int(7)
LEVEL_B = int(8)
LEVEL_C = int(9)

NORMAL = int(1)
CREDIT = int(2)

class Account:
    def __init__(self, ID = None, money = None, name = None):
        self.accID = ID # NOT private
        self.balance = money
        self.cusName = name

    def copy(self, Account):
        self.accID = Account.accID
        self.balance = Account.balance
        self.cusName = Account.cusName

    def getAccID(self):
        return self.accID
    
    def baseDeposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if self.balance < money:
            return 0
        else:
            self.balance -= money
        return money
    def showAccInfo(self) :
        print("계좌번호 : {}".format(self.accID))
        print("이　　름 : {}".format(self.cusName))
        print("잔　　액 : {}".format(self.balance))

class AccountHandler:
    def __init__(self):
        self.accNum = 0
        self.accArr = []

    def showMenu(self) :
        print("----메 뉴----")
        print("1. 계좌개설 ")
        print("2. 입　　금 ")
        print("3. 출　　금 ")
        print("4. 계좌정보 ")
        print("5. 종　　료 ")
    
    def makeAccount(self):
        print("계좌 종류")
        print("1. Normal Account")
        print("2. HighCreditAccount")
        temp = int(input('choose : '))

        if temp == NORMAL :
            self.__makeNormalAccount()
        elif  temp == CREDIT:
            self.__makeCreditAccount()
        else:
            print("ERROR")

    def depositMoney(self):
        id = int(input('ID : '))
        money = int(input('입금액 : '))
        for i in range(self.accNum):
            if self.accArr[i].getAccID() == id :
                self.accArr[i].deposit(money)
                print("입금 완료")
                return
        print("존재하지 않는 ID ")

    def withdrawMoney(self) :
        id = int(input('ID : '))
        money = int(input('입금액 : '))
        for i in range(self.accNum):
            if self.accArr[i].getAccID() == id :
                self.accArr[i].withdraw(money)
                print("출금 완료")
                return
        print("존재하지 않는 ID ")

    def showAllAccInfo(self):
        for temp in self.accArr:
            temp.showAccInfo()
            print("-------------")
    
    def __makeNormalAccount(self):
        id = int(input('ID : '))
        name = input('Name : ')
        balance = int(input('입금 금액 : '))
        interRate = int(input('이율 : '))
        temp = NormalAccount(id, balance, name, interRate)
        self.accArr.append(temp)

    def __makeCreditAccount(self):
        id = int(input('ID : '))
        name = input('Name : ')
        balance = int(input('입금 금액 : '))
        interRate = int(input('이율 : '))
        creditLevel = int(input('신용등급(1 = A, 2 = B, 3 = C) : '))

        if creditLevel == 1:
            temp = HighCreditAccount(id, balance, name, interRate, LEVEL_A)
        elif creditLevel == 2:
            temp = HighCreditAccount(id, balance, name, interRate, LEVEL_B)
        elif creditLevel == 3:
            temp = HighCreditAccount(id, balance, name, interRate, LEVEL_C)
        else:
            print("ERROR")
            quit()
        
        self.accArr.append(temp)
        
class NormalAccount(Account):
    def __init__(self, ID, money, name, rate):
        super().__init__(ID, money, name),
        self.interRate = rate

    def deposit(self, money):
        super().baseDeposit(money)
        super().baseDeposit((money * self.interRate) / 100)

class HighCreditAccount(NormalAccount):
    def __init__(self, ID, money, name, rate, special):
        super().__init__(ID, money, name, rate)
        self.specialRate = special

    def deposit(self, money):
        super().deposit(money)
        super().baseDeposit((money * self.specialRate) / 100)


manager = AccountHandler()

while(True):
    manager.showMenu()
    choice = int(input('choose : '))

    if choice == MAKE:
        manager.makeAccount()
    elif choice == DEPOPSIT:
        manager.depositMoney()
    elif choice == WITHDRAW:
        manager.withdrawMoney()
    elif choice == INQUIRE:
        manager.showAllAccInfo()
    elif choice == EXIT:
        break
    else:
        print("Illegal selection")
