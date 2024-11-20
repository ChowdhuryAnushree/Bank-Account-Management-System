import tkinter
from tkinter import messagebox

# Bank account class
class Bank_Account:
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance
        self.transactions = []

    def deposit_amount(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append('Deposited: $' + str(amount))
        else:
            raise ValueError('Deposit amount must be positive')

    def withdraw_amount(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append('Withdrew: $' + str(amount))
        elif amount <= 0:
            raise ValueError('Withdrawal amount must be positive')
        else:
            raise ValueError('Insufficient funds')

    def current_balance(self):
        return self.balance

    def all_transactions(self):
        return self.transactions


class Savings_Account(Bank_Account):
    def __init__(self, name, password, balance):
        super().__init__(name, password, balance)


# GUI setup
window = tkinter.Tk()
window.title('Welcome to the 6ix Bank!')

# Global variables
user_account = None
username_entry = None
password_entry = None

# Login page
def login_page_gui():
    global username_entry, password_entry
    close_other_screens()

    username_label = tkinter.Label(window, text='Enter your name')
    username_label.pack(pady=10)
    username_entry = tkinter.Entry(window)
    username_entry.pack()

    password_label = tkinter.Label(window, text='Enter your password')
    password_label.pack(pady=10)
    password_entry = tkinter.Entry(window, show='*')
    password_entry.pack()

    login_button = tkinter.Button(window, text='Login', command=login)
    login_button.pack(pady=15)

# Login functionality
def login():
    global user_account
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    for char in username:
        if not (char.isalpha() or char == ' '):
            messagebox.showerror('Error', 'Name can only contain letters and spaces')
            return

    if username != '' and password != '':
        user_account = Savings_Account(username, password,10000)
        main_screen_gui()
    else:
        messagebox.showerror('Error', 'Please enter a valid username and password')

# Main screen
def main_screen_gui():
    close_other_screens()

    welcome_label = tkinter.Label(window, text='Welcome, ' + user_account.name + '!')
    welcome_label.pack(pady=10)

    balance_label = tkinter.Label(window, text='Balance: $' + str((user_account.current_balance())))
    balance_label.pack(pady=10)

    deposit_button = tkinter.Button(window, text='Deposit', command=deposit_screen_gui)
    deposit_button.pack(pady=10)

    withdraw_button = tkinter.Button(window, text='Withdraw', command=withdraw_screen_gui)
    withdraw_button.pack(pady=10)

    transactions_button = tkinter.Button(window, text='View Transactions', command=all_transactions_gui)
    transactions_button.pack(pady=10)

    logout_button = tkinter.Button(window, text='Logout', command=login_page_gui)
    logout_button.pack(pady=15)

# Deposit screen
def deposit_screen_gui():
    close_other_screens()

    deposit_amt_label = tkinter.Label(window, text='Enter amount to deposit')
    deposit_amt_label.pack(pady=10)
    deposit_amt_entry = tkinter.Entry(window)
    deposit_amt_entry.pack(pady=5)

    def deposit_amount():
        try:
            amount = float(deposit_amt_entry.get())
            if amount > 0:
                user_account.deposit_amount(amount)
                messagebox.showinfo('Success', 'Deposited: $' + str((amount)))
                deposit_screen_gui()
            else:
                messagebox.showerror('Error', 'Deposit amount must be greater than zero')
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid numeric amount')

    deposit_button = tkinter.Button(window, text='Deposit', command=deposit_amount)
    deposit_button.pack(pady=5)

    back_button = tkinter.Button(window, text='Back', command=main_screen_gui)
    back_button.pack(pady=10)

# Withdraw screen
def withdraw_screen_gui():
    close_other_screens()

    withdraw_amt_label = tkinter.Label(window, text='Enter amount to withdraw:')
    withdraw_amt_label.pack(pady=10)
    withdraw_amt_entry = tkinter.Entry(window)
    withdraw_amt_entry.pack(pady=5)

    def withdraw_amount():
        try:
            amount = float(withdraw_amt_entry.get())
            if amount <= 0:
                messagebox.showerror('Error', 'Withdrawal amount must be greater than zero')
            elif amount > user_account.current_balance():
                messagebox.showerror('Error', 'Insufficient funds')
            else:
                user_account.withdraw_amount(amount)
                messagebox.showinfo('Success', 'Withdrew: $' + str(amount))
                withdraw_screen_gui()
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid numeric amount')

    withdraw_button = tkinter.Button(window, text='Withdraw', command=withdraw_amount)
    withdraw_button.pack(pady=5)

    back_button = tkinter.Button(window, text='Back', command=main_screen_gui)
    back_button.pack(pady=10)

# Transactions screen
def all_transactions_gui():
    close_other_screens()

    transactions_label = tkinter.Label(window, text='Transaction History')
    transactions_label.pack(pady=10)

    frame = tkinter.Frame(window)
    frame.pack()

    transactions_text = tkinter.Text(frame, height=11, width=40)
    scrollbar = tkinter.Scrollbar(frame)

    transactions_text.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y, padx=5)

    transactions_text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=transactions_text.yview)

    transactions = user_account.all_transactions()
    if len(transactions) != 0:
        for transaction in transactions:
            transactions_text.insert(tkinter.END, transaction + '\n')
    else:
        transactions_text.insert(tkinter.END,'No transactions yet')
    transactions_text.config(state=tkinter.DISABLED)
    transactions_text.pack(pady=10)

    back_button = tkinter.Button(window, text='Back', command=main_screen_gui)
    back_button.pack(pady=10)

# Close all screens
def close_other_screens():
    for screen in window.winfo_children():
        screen.destroy()

# Starting the GUI application
login_page_gui()
window.mainloop()