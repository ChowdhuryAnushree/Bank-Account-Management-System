import tkinter
from tkinter import ttk
from tkinter import messagebox

class Bank_Account:
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance
        self.transactions = []

    def deposit_amount(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append("Deposited: $" + str(amount))
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw_amount(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append("Withdrew: $" + str(amount))
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        else:
            raise ValueError("Insufficient funds.")

    def current_balance(self):
        return self.balance

    def all_transactions(self):
        return self.transactions

class Savings_Account(Bank_Account):
    def __init__(self, name, password, balance):
        super().__init__(name, password, balance)


window = tkinter.Tk()
window.title('Welcome to the 6ix Bank!')

def on_start():
    login_page_gui()

def login_page_gui():
    clear_window()
    name_label = tkinter.Label(window, text="Enter your name to log in")
    name_label.pack(pady=10)
    name_entry = tkinter.Entry(window)
    name_entry.pack()

    password_label = tkinter.Label(window, text="Enter your password")
    password_label.pack(pady=10)
    password_entry = tkinter.Entry(window, show="*")
    password_entry.pack()

    login_button = tkinter.Button(window, text='Login',command=main_screen_gui)  # add login button functionality
    login_button.pack(pady=15)

def main_screen_gui():
    clear_window()
    welcome_label = tkinter.Label(window, text="Welcome, " + '{enter name}' + "!") #need to fetch username
    welcome_label.pack()

    balance_label = tkinter.Label(window,text="Balance:"+str() )
    balance_label.pack(pady=10)

    deposit_button = tkinter.Button(window, text='Deposit',command= deposit_screen_gui)
    deposit_button.pack(pady=10)

    withdraw_button = tkinter.Button(window, text='Withdraw',command=withdraw_screen_gui)
    withdraw_button.pack()

    transactions_button = tkinter.Button(window, text='All Transactions')  # add functionality
    transactions_button.pack(pady=10)

    logout_button = tkinter.Button(window, text='Logout',command=login_page_gui)
    logout_button.pack(pady=15)

def deposit_screen_gui():
    clear_window()
    deposit_amt_label = tkinter.Label(window, text="Enter amount to deposit")
    deposit_amt_label.pack(pady=10)
    deposit_amt_label = tkinter.Entry(window)
    deposit_amt_label.pack()

    deposit_button = tkinter.Button(window, text='Deposit')  # add functionality
    deposit_button.pack(pady=5)

    back_button = tkinter.Button(window, text='Back',command=main_screen_gui)  # add functionality
    back_button.pack(pady=10)

def withdraw_screen_gui():
    clear_window()
    withdraw_amt_label = tkinter.Label(window, text="Enter amount to withdraw")
    withdraw_amt_label.pack(pady=10)
    withdraw_amt_label = tkinter.Entry(window)
    withdraw_amt_label.pack()

    withdraw_button = tkinter.Button(window, text='Withdraw')  # add functionality
    withdraw_button.pack(pady=5)

    back_button = tkinter.Button(window, text='Back',command=main_screen_gui)  # add functionality
    back_button.pack(pady=10)

def all_transactions_gui():
    clear_window()
    #write logic




def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

main_screen_gui()
window.mainloop()