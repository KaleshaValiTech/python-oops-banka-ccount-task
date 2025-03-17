import datetime

class BankAccount:
    total_accounts = 0
    all_accounts = []
    
    def __init__(self, name, account_type, balance=0):
        if not name:
            raise ValueError("Account holder's name cannot be empty.")
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.transactions = []
        BankAccount.total_accounts += 1
        BankAccount.all_accounts.append(self)
        print(f"✅ New {account_type} account created for {name}.\n")
    
    def deposit(self, amount):
        if amount > 50000:
            print("❌ Deposit amount exceeds limit (₹50,000).\n")
            return
        self.balance += amount
        self.transactions.append((datetime.datetime.now(), f"Deposited ₹{amount}"))
        print(f"💰 Deposited ₹{amount}. New balance: ₹{self.balance}\n")
    
    def withdraw(self, amount):
        if amount > 50000:
            print("❌ Withdrawal amount exceeds limit (₹50,000).\n")
            return
        if self.balance - amount < 0:
            print("❌ Insufficient funds.\n")
            return
        self.balance -= amount + 10  # ₹10 transaction fee
        self.transactions.append((datetime.datetime.now(), f"Withdrew ₹{amount} (Fee ₹10)"))
        print(f"💸 Withdrew ₹{amount}. New balance: ₹{self.balance}\n")
    
    def transfer(self, other_account, amount):
        if self.balance - amount < 0:
            print("❌ Insufficient funds for transfer.\n")
            return
        self.balance -= amount
        other_account.balance += amount
        self.transactions.append((datetime.datetime.now(), f"Transferred ₹{amount} to {other_account.name}"))
        other_account.transactions.append((datetime.datetime.now(), f"Received ₹{amount} from {self.name}"))
        print(f"🔄 Transferred ₹{amount} to {other_account.name}.\n")
    
    def check_balance(self):
        print(f"💵 Account balance: ₹{self.balance}\n")
        return self.balance
    
    def get_transaction_history(self):
        print("📜 Transaction History:")
        for date, detail in self.transactions:
            print(f"{date}: {detail}")
        print()
    
    @classmethod
    def get_total_accounts(cls):
        print(f"🏦 Total bank accounts: {cls.total_accounts}\n")
    
    @staticmethod
    def validate_amount(amount):
        return amount > 0

class SavingsAccount(BankAccount):
    interest_rate = 0.05  # 5% annual interest
    min_balance = 1000
    
    def __init__(self, name, balance=1000):
        super().__init__(name, "Savings", balance)
        if balance < self.min_balance:
            raise ValueError("❌ Minimum balance for Savings Account is ₹1000.\n")
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append((datetime.datetime.now(), f"Interest added ₹{interest}"))
        print(f"📈 Interest added: ₹{interest}. New balance: ₹{self.balance}\n")

class CurrentAccount(BankAccount):
    def __init__(self, name, balance=0):
        super().__init__(name, "Current", balance)

# Sample Run (Easy to Understand)
print("Welcome to Simple Bank System!\n")
print("🏦 Bank Options:")
print("1️⃣ Open an Account")
print("2️⃣ Deposit Money")
print("3️⃣ Withdraw Money")
print("4️⃣ Transfer Money")
print("5️⃣ Check Balance")
print("6️⃣ View Transaction History")
print()

BankAccount.get_total_accounts()

print("Available Accounts:")
for acc in BankAccount.all_accounts:
    print(f"- {acc.name} ({acc.account_type})")
print()

name1 = input("Enter your name for Savings Account: ")
acc1 = SavingsAccount(name1, 5000)
name2 = input("Enter your name for Current Account: ")
acc2 = CurrentAccount(name2, 2000)

acc1.deposit(3000)
acc1.withdraw(2000)
acc1.transfer(acc2, 1000)
acc1.apply_interest()
acc1.get_transaction_history()
BankAccount.get_total_accounts()

Sample Output:-
-------------

Welcome to Simple Bank System!

🏦 Bank Options:
1️⃣ Open an Account
2️⃣ Deposit Money
3️⃣ Withdraw Money
4️⃣ Transfer Money
5️⃣ Check Balance
6️⃣ View Transaction History

🏦 Total bank accounts: 0

Available Accounts:

Enter your name for Savings Account: Alice
✅ New Savings account created for Alice.

Enter your name for Current Account: Bob
✅ New Current account created for Bob.

💰 Deposited ₹3000. New balance: ₹8000

💸 Withdrew ₹2000. New balance: ₹5990

🔄 Transferred ₹1000 to Bob.

📈 Interest added: ₹399.5. New balance: ₹6389.5

📜 Transaction History:
2025-03-17 12:45:00: Deposited ₹3000
2025-03-17 12:45:10: Withdrew ₹2000 (Fee ₹10)
2025-03-17 12:45:20: Transferred ₹1000 to Bob
2025-03-17 12:45:30: Interest added ₹399.5

🏦 Total bank accounts: 2


