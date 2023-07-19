from functions import menu, deposit, withdrawal, show_statement, register_user, register_bank_account

balance = 0
LIMIT = 500
statement = ""
withdrawal_number = 0
WITHDRAWAL_LIMIT = 3

while True:
    option = menu()
    
    if option == "D":
        value_deposit = float(input("How much do you want to deposit?\nR$"))
        balance, statement = deposit(value_deposit, balance, statement)
    
    elif option == "W":
        value_withdrawal = float(input("How much do you want to Withdraw?\nR$"))
        balance, statement, withdrawal_number = withdrawal(value_withdrawal, balance, statement, LIMIT, withdrawal_number, WITHDRAWAL_LIMIT)
    
    elif option == "S":
        show_statement(balance, statement)
    
    elif option == "E":
        break
    
    else:
        print("Invalid option, please select again the desired operation.")