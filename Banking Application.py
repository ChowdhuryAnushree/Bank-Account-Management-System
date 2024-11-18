import tkinter
from tkinter import messagebox

# Bank account classes
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


# GUI setup
window = tkinter.Tk()
window.title("Welcome to the 6ix Bank!")

# Global variables
user_account = None
username_entry = None
password_entry = None

# Login page
def login_page_gui():
    global username_entry, password_entry
    clear_window()

    username_label = tkinter.Label(window, text="Enter your username")
    username_label.pack(pady=10)
    username_entry = tkinter.Entry(window)
    username_entry.pack()

    password_label = tkinter.Label(window, text="Enter your password")
    password_label.pack(pady=10)
    password_entry = tkinter.Entry(window, show="*")
    password_entry.pack()

    login_button = tkinter.Button(window, text="Login", command=login)
    login_button.pack(pady=15)

# Login functionality
def login():
    global user_account
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    if username != "" and password != "":
        user_account = Savings_Account(username, password, 0)
        main_screen_gui()
    else:
        messagebox.showerror("Error", "Please enter a valid username and password.")

# Main screen
def main_screen_gui():
    clear_window()

    welcome_label = tkinter.Label(window, text="Welcome, " + user_account.name + "!")
    welcome_label.pack(pady=10)

    balance_label = tkinter.Label(window, text="Balance: $" + str((user_account.current_balance())))
    balance_label.pack(pady=10)

    deposit_button = tkinter.Button(window, text="Deposit", command=deposit_screen_gui)
    deposit_button.pack(pady=10)

    withdraw_button = tkinter.Button(window, text="Withdraw", command=withdraw_screen_gui)
    withdraw_button.pack(pady=10)

    transactions_button = tkinter.Button(window, text="View Transactions", command=all_transactions_gui)
    transactions_button.pack(pady=10)

    logout_button = tkinter.Button(window, text="Logout", command=login_page_gui)
    logout_button.pack(pady=15)

# Deposit screen
def deposit_screen_gui():
    clear_window()

    deposit_amt_label = tkinter.Label(window, text="Enter amount to deposit")
    deposit_amt_label.pack(pady=10)
    deposit_amt_entry = tkinter.Entry(window)
    deposit_amt_entry.pack(pady=5)

    def deposit_amount():
        try:
            amount = float(deposit_amt_entry.get())
            if amount > 0:
                user_account.deposit_amount(amount)
                messagebox.showinfo("Success", "Deposited: $" + str(round(amount, 2)))
                main_screen_gui()
            else:
                messagebox.showerror("Error", "Deposit amount must be greater than zero.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric amount.")

    deposit_button = tkinter.Button(window, text="Deposit", command=deposit_amount)
    deposit_button.pack(pady=5)

    back_button = tkinter.Button(window, text="Back", command=main_screen_gui)
    back_button.pack(pady=10)

# Withdraw screen
def withdraw_screen_gui():
    clear_window()

    withdraw_amt_label = tkinter.Label(window, text="Enter amount to withdraw:")
    withdraw_amt_label.pack(pady=10)
    withdraw_amt_entry = tkinter.Entry(window)
    withdraw_amt_entry.pack(pady=5)

    def withdraw_amount():
        try:
            amount = float(withdraw_amt_entry.get())
            user_account.withdraw_amount(amount)
            messagebox.showinfo("Success", "Withdrew: $" + str(round(amount, 2)))
            main_screen_gui()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    withdraw_button = tkinter.Button(window, text="Withdraw", command=withdraw_amount)
    withdraw_button.pack(pady=5)

    back_button = tkinter.Button(window, text="Back", command=main_screen_gui)
    back_button.pack(pady=10)

# Transactions screen
def all_transactions_gui():
    clear_window()

    transactions_label = tkinter.Label(window, text="Transaction History:")
    transactions_label.pack(pady=10)

    transactions_text = tkinter.Text(window, height=10, width=40)
    transactions = user_account.all_transactions()
    if transactions:
        transactions_text.insert(tkinter.END, "\n".join(transactions))
    else:
        transactions_text.insert(tkinter.END, "No transactions yet.")
    transactions_text.config(state=tkinter.DISABLED)
    transactions_text.pack(pady=10)

    back_button = tkinter.Button(window, text="Back", command=main_screen_gui)
    back_button.pack(pady=10)

# Clear all widgets
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# Initialize the GUI
login_page_gui()
window.mainloop()