# For this challenge, create a bank account class that has two attributes:
# * owner
# * balance
#
# and two methods:
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,depositAmount):
        self.balance += depositAmount
        print(self)

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.balance:
            print("Error: balance amount less than withdraw amount. Transaction cancelled")
        else:
            self.balance = self.balance - withdrawAmount
            print("Withdrawal Complete!")
            print(self)

    def __repr__(self):
        formattedString = "{}'s account balance is ${}".format(self.owner, self.balance)
        return formattedString


# 1. Instantiate the class
acct1 = Account('Xee',100)
# 2. Print the object
print(acct1)
# 3. Show the account owner attribute
print(acct1.owner)
# 4. Show the account balance attribute
print(acct1.balance)
# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)