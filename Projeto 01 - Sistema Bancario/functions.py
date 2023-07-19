#positional only
def deposit(balance, value, statement):
    ...
    return balance, statement

#keyword only
def withdrawal(balance, value, statement, LIMIT, withdrawal_number, WITHDRAWAL_LIMIT):
    ...
    return balance, statement

#Positional (balance) and Keyword (statement)
def statement(balance, statement):
    ...

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