def menu():
    text = """
    [D] Deposit
    [W] Withdrawal
    [S] Statement
    [E] Exit

    => """
    
    option = input(text).upper()
    return option

#positional only
def deposit(value_deposit, balance, statement):
    if value_deposit <= 0:
        print("Please enter a valid number!")
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
        print("Please enter a valid number!")
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
#CPF must be unformatted, and can't be 2 identical CPF
def register_user():
    ...

#customer's account
#dict = ["agency": "0001", account number, customer]
#A customer can have more than one account, but one account can't have more than one costumer
def register_bank_account():
    ...

#optional
def show_accounts():
    ...

#optional
def show_users():
    ...