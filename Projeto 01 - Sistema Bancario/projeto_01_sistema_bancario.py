from functions import deposit, withdrawal, statement, register_user, register_bank_account


menu = """
[D] Deposit
[W] Withdrawal
[S] Statement
[E] Exit

=> """

balance = 0
LIMIT = 500
statement = ""
withdrawal_number = 0
WITHDRAWAL_LIMIT = 3

while True:
    option = input(menu).upper()
    
    if option == "D":
        deposit = float(input("How much do you want to deposit?\nR$"))
        
        if deposit <= 0:
            print("Please enter a valid number!")
        else:
            balance += deposit
            statement += f"Deposit R${deposit:.2f}\n"
            print(f"Your new balance is R${balance:.2f}!")
    
    elif option == "W":
        withdrawal = int(input("How much do you want to Withdraw?\nR$"))
        
        if withdrawal_number >= WITHDRAWAL_LIMIT:
            print("You have already reached your daily withdrawal limits!")
        elif withdrawal <= 0:
            print("Please enter a valid number!")
        elif withdrawal > balance:
            print("Not enough balance in your account!")
        elif withdrawal > LIMIT:
            print(f"Sorry, your withdraw limit is R${LIMIT}!")
        else:
            balance -= withdrawal
            statement += f"Withdrawal R${withdrawal:.2f}\n"
            withdrawal_number += 1
            print(f"Your new balance is R${balance:.2f}!")
    
    elif option == "S":
        print("================Statement!================")
        print("You haven't performed any operations yet!" if not statement else statement)
        print(f"\nBalance: R${balance:.2f}")
        print("==========================================")
    
    elif option == "E":
        break
    
    else:
        print("Invalid option, please select again the desired operation.")