#Create account class with 2 attributes :balance and acc. no.
#create method for debit ,credit, and printing the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance= bal
        self.accountno= acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs", self.balance, "was debited")
        print("totol balance=", self.get_balance)
    
    def credit(self, amount):
        self.balance += amount
        print("Rs", "self.balance", "was credited")
        print("totol balance=",self.get_balance ) 
    
    
acc1= Account(10000, 123456)
print(acc1.balance)
print(acc1.accountno)
