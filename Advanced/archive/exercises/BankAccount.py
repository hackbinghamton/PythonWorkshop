# Prompt: Create a BankAccount class that allows a user to create various instance objects and withdraw from/deposit to them.

class BankAccount:
    def __init__(self):
        # TODO: What instance variable(s) do you need?

    def withdraw(self, amount):
        # TODO: Implement logic for withdraw

    def deposit(self, amount):
        # TODO: Implement logic for deposit

    def getBalance(self):
        # TODO: Implement logic for getting balance

if __name__ == "__main__":
    a = BankAccount()
    b = BankAccount()
    a.deposit(100)
    b.deposit(50)
    print(a.getBalance())
    print(b.getBalance())
    a.withdraw(75)
    b.deposit(5)
    assert(a.getBalance() < b.getBalance())
