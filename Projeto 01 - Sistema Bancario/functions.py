users = {}
accounts = {}
INVALID_OPTION = "Please enter a valid number!"
MENU_TEXT = """    [D] Deposit   
    [W] Withdrawal
    [S] Statement
    [I] Insert User
    [C] create Account
    [U] Show Users
    [A] Show Accounts
    [E] Exit
    => """

def menu():
    option = input(MENU_TEXT).upper()
    return option

#positional only
def deposit(value_deposit, balance, statement):
    if value_deposit <= 0:
        print(INVALID_OPTION)
    else:
        balance += value_deposit
        statement += f"Deposit R${value_deposit:.2f}\n"
        print(f"Your new balance is R${balance:.2f}!")
    return balance, statement

#keyword only
def withdrawal(value_withdrawal, balance, statement, LIMIT, withdrawal_number, WITHDRAWAL_LIMIT):
    if withdrawal_number >= WITHDRAWAL_LIMIT:
        print("You have already reached your daily withdrawal limits!")
    elif value_withdrawal <= 0:
        print(INVALID_OPTION)
    elif value_withdrawal > balance:
        print("Not enough balance in your account!")
    elif value_withdrawal > LIMIT:
        print(f"Sorry, your withdraw limit is R${LIMIT}!")
    else:
        balance -= value_withdrawal
        statement += f"Withdrawal R${value_withdrawal:.2f}\n"
        withdrawal_number += 1
        print(f"Your new balance is R${balance:.2f}!")
    return balance, statement, withdrawal_number

#Positional (balance) and Keyword (statement)
def show_statement(balance, statement):
    print("================Statement!================")
    print("You haven't performed any operations yet!" if not statement else statement)
    print(f"\nBalance: R${balance:.2f}")
    print("==========================================")

#bank customer information
#dict = [name, date of birth, CPF, address]
#address = "address, number - neighborhood - city/state"
#CPF must be unformatted, and can't have 2 identical CPF
def register_user():
    cpf = input("Please inform the customer's CPF: ")
    if cpf in users:
        print("This user is already registered!")
    else:
        name = input("Please inform the customer's name: ")
        date_of_birth = input("Please inform the customer's date of birth: ")
        address = input("Please inform the customer's street name: ")
        number = input("Please inform the customer's house number: ")
        neighborhood = input("Please inform the customer's neighborhood: ")
        city = input("Please inform the customer's city: ")
        state = input("Please inform the customer's state: ")
        users.update({cpf: {"name": name, "date_of_birth": date_of_birth, "address": f"{address}, {number} - {neighborhood} - {city}/{state}"}})
        ...
        print(f"The client {cpf} was registered with success")
        print(users)

#customer's account
#dict = ["agency": "0001", account number, customer]
#A customer can have more than one account, but one account can't have more than one costumer
def register_bank_account():
    ...

#optional
def show_users():
    if users == True:
        print("There is no User registered yet!")
    else:
        print(users)

#optional
def show_account():
    if accounts == True:
        print("There is no accounts registered yet!")
    else:
        print(accounts)