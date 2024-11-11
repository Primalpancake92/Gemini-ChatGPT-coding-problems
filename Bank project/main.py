import Account
from Bank import Bank

if __name__ == "__main__":
    # Create a bank instance
    bank = Bank()

    # Create accounts for Alice and Bob
    alice_account = bank.create_account("Alice", 500)
    bob_account = bank.create_account("Bob", 300)

    # Check account details
    bank.get_account("Alice")
    bank.get_account("Bob")

    # Perform a transfer
    alice_account.transfer(100, bob_account)

    # Check updated account balances
    bank.get_account("Alice")
    bank.get_account("Bob")
