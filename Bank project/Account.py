class BankAccount:
    def __init__(self, owner_name: str, balance: float): 
        self.owner_name = owner_name
        self.balance = balance
        
    
    def deposit(self, amount: float):
        self.balance += amount
        
    
    def withdraw(self, amount: float):
        self.balance -= amount
        
    
    def get_balance(self):
        return self.balance

    
    def transfer(self, amount: float, other_account : "BankAccount"):
        if self.balance >= amount: 
            