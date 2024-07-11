class Account:

    def __init__(self, name, accountNum):
        self.balance = 0
        self.name = name
        self.accountNum = accountNum

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def printBalance(self, balance):
        return self.balance
