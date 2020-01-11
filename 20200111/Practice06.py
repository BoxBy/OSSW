# https://github.com/BoxBy/Cpp/tree/master/20191031 : Cpp to Python

RISK_A = int(3)
RISK_B = int(2)
RISK_C = int(1)

class Employee :
    def __init__(self, name) :
        self.__name = name

    def printname(self) :
        print("Name : {}".format(self.__name))
    
class PermanentWorker(Employee) :
    def __init__(self, name, salary) :
        super().__init__(name)
        self.__salary = salary

    def getPay(self) :
        return self.__salary

    def showInfo(self) :
        super().printname()
        print("Salary : {}".format(self.getPay()))

class TemporaryWorker(Employee) :
    def __init__(self, name, pay) :
        super().__init__(name)
        self.__payPerHour = pay
        self.__workTime = 0

    def addWorkTime(self, workTime) :
        self.__workTime += workTime
    
    def getPay(self) :
        return self.__workTime * self.__payPerHour

    def showInfo(self) :
        super().printname()
        print("workTime * payPerHour : {}".format(self.getPay()))

class SalesWorker(PermanentWorker) :
    def __init__(self, name, salary, bonusRatio) :
        super().__init__(name, salary)
        self.__bonusRatio = 0.1 * bonusRatio

    def addSalesResult(self, salesResult) :
        self.__salesResult = salesResult

    def getPay(self) :
        return super().getPay() + (self.__salesResult * self.__bonusRatio)

    def showInfo(self) : 
        Employee.printname(self)
        print("Pay : {}".format(self.getPay()))

class ForeignSalesWorker(SalesWorker) :
    def __init__(self, name, salary, bonusRatio, riskLevel) :
        super().__init__(name, salary, bonusRatio)
        self.__riskLevel = riskLevel

    def getRiskPay(self) : 
        return super().getPay() * self.__riskLevel * 0.1

    def getPay(self) :
        return PermanentWorker.getPay(self) + self.getRiskPay()
    
    def showInfo(self) : 
        Employee.printname(self)
        print("Salary : {}".format(PermanentWorker.getPay(self)))
        print("Risk Pay : {}".format(self.getRiskPay()))
        print("Total : {}".format(self.getPay()))

class EmployeeHandler :
    def __init__(self) :
        self.__emp = []

    def addEmployee(self, emp) :
        self.__emp.append(emp)

    def showAllInfo(self) :
        for empPrint in self.__emp :
            empPrint.showInfo()
    
    def showTotalSalary(self) :
        total = 0
        for emp in self.__emp :
            total += emp.getPay()
        print("TotalSalary : {}".format(total))
        del total
    
    def __del__(self) :
        del self.__emp

handler = EmployeeHandler()

per1 = PermanentWorker("Kim", 1000)
handler.addEmployee(per1)
per2 = PermanentWorker("Lee", 1500)
handler.addEmployee(per2)

alba = TemporaryWorker("Jung", 700)
alba.addWorkTime(5)
handler.addEmployee(alba)

seller = SalesWorker("Hong", 1000, 0.1)
seller.addSalesResult(7000)
handler.addEmployee(seller)

fseller = ForeignSalesWorker("Park", 1000, 0.1, RISK_B)
fseller.addSalesResult(7000)
handler.addEmployee(fseller)

handler.showAllInfo()
handler.showTotalSalary()

del handler