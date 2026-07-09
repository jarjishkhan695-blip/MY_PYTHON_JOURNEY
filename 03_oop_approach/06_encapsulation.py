"""
Encapsulation in Python

Encapsulation means keeping data and related methods together inside a class.
A leading underscore is commonly used to show that a variable is intended for internal use.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Invalid withdrawal amount")

    def show_balance(self):
        print("Owner:", self.owner)
        print("Balance:", self._balance)


account = BankAccount("Jarjish", 1000)
account.deposit(500)
account.withdraw(300)
account.show_balance()
