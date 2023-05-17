
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        print("Account Ctor......")

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):
    def debit(self):
        print("Amount #### credited into the account.......")

    def getBalance(self):
        print("Balance in the account ending ##123 is ######")


sav = Savings()
sav.debit()
sav.getBalance()

