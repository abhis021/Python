import sqlite3
from getpass import getpass

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into your account. Current balance is ${self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from your account. Current balance is ${self.balance}.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance in your account is ${self.balance}.")


class BankDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts
            (account_number TEXT PRIMARY KEY, account_holder TEXT, balance REAL)
        """)
        self.conn.commit()

    def insert_account(self, account_number, account_holder, initial_balance=0):
        self.cursor.execute("INSERT INTO accounts VALUES (?, ?, ?)", (account_number, account_holder,
initial_balance))
        self.conn.commit()
        print(f"Account {account_number} created successfully.")

    def get_account(self, account_number):
        self.cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,))
        result = self.cursor.fetchone()
        if result:
            return BankAccount(result[0], result[1], result[2])
        else:
            print(f"Account number {account_number} does not exist.")
            return None

    def update_balance(self, account_number, new_balance):
        self.cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance,
account_number))
        self.conn.commit()
        print(f"Updated balance for account {account_number} to ${new_balance}.")

    def delete_account(self, account_number):
        self.cursor.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))
        self.conn.commit()
        print(f"Account number {account_number} deleted successfully.")


class Bank:
    def __init__(self):
        self.db = BankDatabase('bank.db')

    def create_account(self, account_number, account_holder, initial_balance=0):
        if not self.db.get_account(account_number):
            self.db.insert_account(account_number, account_holder, initial_balance)
        else:
            print(f"Account {account_number} already exists.")

    def display_account(self, account_number):
        account = self.db.get_account(account_number)
        if account:
            print(f"Account Number: {account.account_number}")
            print(f"Account Holder: {account.account_holder}")
            print(f"Balance: ${account.balance}")
        else:
            print("Account number does not exist.")

    def update_balance(self, account_number, new_balance):
        self.db.update_balance(account_number, new_balance)

    def delete_account(self, account_number):
        self.db.delete_account(account_number)


def get_input(prompt):
    while True:
        value = input(prompt)
        if value:  # Check if the input is not empty
            return value
        else:
            print("Please enter a valid value.")


def main():
    bank = Bank()

    while True:
        print("\nBanking Application Menu:")
        print("1. Create Account")
        print("2. Display Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            account_number = get_input("Enter account number (default is generated): ")
            if not account_number:
                account_number = f"A-{len(bank.db.get_accounts()) + 1}"
            else:
                account_number = account_number.upper()
            account_holder = input("Enter your name: ")
            initial_balance = float(input("Enter the initial balance (default is $0): ") or 0)
            bank.create_account(account_number, account_holder, initial_balance)
        elif choice == "2":
            account_number = get_input("Enter the account number to display: ")
            if account_number:
                bank.display_account(account_number.upper())
        elif choice == "3":
            account_number = input("Enter the account number to deposit into: ")
            amount = float(input("Enter the amount to deposit: "))
            bank.update_balance(account_number, 0)  # Update balance
            account = bank.db.get_account(account_number)
            if account:
                account.deposit(amount)
        elif choice == "4":
            account_number = input("Enter the account number to withdraw from: ")
            amount = float(input("Enter the amount to withdraw: "))
            bank.update_balance(account_number, 0)  # Update balance
            account = bank.db.get_account(account_number)
            if account:
                account.withdraw(amount)
        elif choice == "5":
            account_number = input("Enter the account number to check balance: ")
            bank.display_account(account_number.upper())
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()