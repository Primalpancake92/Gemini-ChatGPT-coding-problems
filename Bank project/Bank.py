import Account

class Bank:
    def __init__(self):
        self.accounts = []
        
    
    def create_account(self, owner_name: str, initial_balance: float):
        new_account = Account(owner_name, initial_balance)
        self.accounts.append(new_account)
        return new_account
    
    
    def get_account(self, owner_name: str):
        for account in self.accounts: 
            if account == owner_name:
                print(f"Account holder: {account.owner_name}\nBalance: {account.balance}")