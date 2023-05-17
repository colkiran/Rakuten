
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass


class Manager(Employee):

    def doJob(self):
        print("Manager's Job........")

class Developer(Employee):

    def doJob(self):
        print("Developer's Job.......")


def BankFun(emp):           # polymorphism
    print('Bank Job Started.......')
    emp.doJob()
    print("Bank Job Ended.......")
    print("-" * 40)

Mike = Manager()
David = Developer()

BankFun(Mike)
BankFun(David)

