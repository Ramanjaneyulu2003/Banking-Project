from os import system
system("cls")
import os

class Account:
    def __init__(self, acc_number, acc_holder, balance=0):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} into account {self.acc_number}."
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount} from account {self.acc_number}."
        else:
            return "Insufficient funds."
    
    def get_balance(self):
        return f"Current balance of account {self.acc_number}: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account):
        self.accounts[account.acc_number] = account
    
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for acc_number, account in self.accounts.items():
                f.write(f"{acc_number},{account.acc_holder},{account.balance}\n")
    
    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                for line in f:
                    acc_number, acc_holder, balance = line.strip().split(',')
                    self.add_account(Account(acc_number, acc_holder, float(balance)))
    
    def get_account(self, acc_number):
        return self.accounts.get(acc_number)


def main():
    bank = Bank()
    bank.load_from_file("bank_data.txt")
    
    while True:
        print("\n1. Create a new account")
        print("2. Deposit money into an account")
        print("3. Withdraw money from an account")
        print("4. Check balance of an account")
        print("5. Save and exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            acc_number = input("Enter account number: ")
            acc_holder = input("Enter account holder name: ")
            account = Account(acc_number, acc_holder)
            bank.add_account(account)
            print("Account created successfully.")
        
        elif choice == '2':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(acc_number)
            if account:
                print(account.deposit(amount))
            else:
                print("Account not found.")
        
        elif choice == '3':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(acc_number)
            if account:
                print(account.withdraw(amount))
            else:
                print("Account not found or insufficient funds.")
        
        elif choice == '4':
            acc_number = input("Enter account number: ")
            account = bank.get_account(acc_number)
            if account:
                print(account.get_balance())
            else:
                print("Account not found.")
        
        elif choice == '5':
            bank.save_to_file("bank_data.txt")
            print("Data saved successfully. Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
