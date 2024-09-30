# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Simple Bank Account Management System

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}.")
        else:
            print("Invalid withdrawal amount. Check your balance or amount.")

    def check_balance(self):
        print(f"Account balance: ${self.balance}.")

def create_account():
    name = input("Enter account holder's name: ")
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(name, account_number, initial_balance)

def main():
    accounts = {}
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print("Account created successfully.")
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if account_number in accounts:
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")
        
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if account_number in accounts:
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")
        
        elif choice == '4':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found.")
        
        elif choice == '5':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
