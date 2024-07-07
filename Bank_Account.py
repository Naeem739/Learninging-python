class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_winthdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposit (self,amount):
        if amount > 0: 
            self.balance += amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient Balance")
        else:
           self.balance -= amount
        

my = Bank(500)
my.deposit(100)
my.withdraw(300)
my.balance
