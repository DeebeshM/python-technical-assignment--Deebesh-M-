import random

# ------------------- BankAccount Class -------------------
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"✅ Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"✅ Withdrawn {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"💰 Current balance: {self.balance}")

    def __str__(self):
        return f"Account Number: {self.account_number}\nHolder: {self.account_holder}\nBalance: {self.balance}"


# ------------------- Functions -------------------
accounts = []

def create_account():
    name = input("Enter account holder name: ")
    acc_num = random.randint(10000, 99999)
    account = BankAccount(acc_num, name)
    accounts.append(account)
    print(f"✅ Account created successfully! Account Number: {acc_num}")

def find_account():
    acc_num = input("Enter account number: ")
    for acc in accounts:
        if str(acc.account_number) == acc_num:
            return acc
    print("❌ Account not found.")
    return None

def deposit_money():
    acc = find_account()
    if acc:
        try:
            amount = float(input("Enter amount to deposit: "))
            acc.deposit(amount)
        except ValueError:
            print("❌ Invalid amount.")

def withdraw_money():
    acc = find_account()
    if acc:
        try:
            amount = float(input("Enter amount to withdraw: "))
            acc.withdraw(amount)
        except ValueError:
            print("❌ Invalid amount.")

def check_balance():
    acc = find_account()
    if acc:
        acc.check_balance()

def view_account_info():
    acc = find_account()
    if acc:
        print("\n--- Account Info ---")
        print(acc)
        print("-------------------")


# ------------------- Main Menu -------------------
def main():
    while True:
        print("\n===== Bank Account Management System =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Account Info")
        print("6. Exit")
        choice = input("> ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_account_info()
        elif choice == "6":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
