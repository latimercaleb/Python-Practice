# Bank Project
class Acc:
    def __init__(self,holder,num,bal,cred = 1000):
        self.Holder = holder
        self.Num = num
        self.Bal = bal
        self.Cred = cred
        
    def  deposit(self,amt):
        self.Bal += amt
        return ("{0} deposited to account".format(amt))
    
    def  withdraw(self,amt):
        if(self.Bal - amt < self.Cred):
            print  ("Insufficient Funds")
        else:
            self.Bal -= amt
            return "The new balance is {0}".format(self.Bal)
        
    def  showBal(self):
        print(self.Bal)
        
    def transfer(self,target,amt):
        if(self.Bal - amt < self.Cred):
            print("Insufficient Credit")
        else:
            self.Bal -= amt
            target.Bal += amt
            return "The new balance is {0}".format(self.Bal)
