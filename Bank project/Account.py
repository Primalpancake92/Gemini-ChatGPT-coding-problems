class BankAccount:
    def __init__(self, owner_name: str, balance: float): 
        self.owner_name = owner_name
        self.balance = balance
        
    
    def deposit(self, amount: float):
        self.balance += amount
        
    
    def withdraw(self, amount: float):
        if self.balance < amount:
            print("There is an insufficient balance.")
        self.balance -= amount
        
    
    def get_balance(self):
        return self.balance

    
    def transfer(self, amount: float, other_account : "BankAccount"):
        if self.balance >= amount: 
            self.withdraw(amount)
            other_account.deposit(amount)
        print(f"{self.balance} is insufficient to transfer.")
        
    