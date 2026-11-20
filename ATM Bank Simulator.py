'''3. ATM Banking Simulator 
Beginner – Intermediate 
Concepts: Nested conditions, loops, functions 
Requirements 
• Verify a PIN. 
• Display balance, deposit, withdrawal, and exit options. 
• Prevent withdrawals exceeding the available balance. 
• Reject invalid amounts. 
• Use separate functions for deposit, withdrawal, and balance enquiry. 
Bonus: Allow only three PIN attempts. '''

def bank():
    
    balance = 30000

    def check_balance():
        return balance
    def deposite(balance,amount):
        return balance + amount

    def withdrawl(balance,amount):
        return balance - amount

    password = "2345"
    attempt = 1

    while attempt <= 3:
        pin = input("enter you pin : ")
            
        if pin == password:
            print("Login Successful!")
            break
        else:   
            attempt += 1
            if attempt > 3:
                print("Account Blocked...")
                break
            else:
                print("Wrong Password..")
            
    while True:
            print("---Menu---")
            print("1.Display Balance..")
            print("2.Deposite...")
            print("3.Withdrawl...")
            print("4.Exit..")
                
            choice = input("enter your choice : ")
                
            if choice == "4":
                print("Thank You...")
                break
                
            if choice not in "1234":
                print("Invalid Choice...")
                continue
                
            if choice == "1":
                print(f"Current Balance : {check_balance()}")
            elif choice == "2":
                amount = int(input("enter the amount : "))
                if amount <= 0:
                    print("Invalid Amount...")   
                else:    
                    balance = deposite(check_balance(),amount)
                    print("Your Amount Deposite Successfully!")
                    check = input("Check Current Balance (Y/N)")
                        
                    if check == "y":
                        print(f"Current Balance : {balance}")
                    elif check == "n":
                        print("Returning to Menu...")
                    else:
                        print("Invalid Choice....")
                
            elif choice == "3":
                amount = int(input("enter the amount : "))
                if amount <= 0:
                    print("Invalid Amount...")
                elif amount > balance:
                    print("Insufficient Balance...")
                else:
                    balance = withdrawl(check_balance(),amount)
                    print("Your Amount withdrawl Successfully!")
                    check = input("Check Current Balance (Y/N)")
                    if check == "y":
                        print(f"Current Balance : {balance}")
                    elif check == "n":
                        print("Returning to Menu...")
                    else:
                        print("Invalid Choice....")    

bank()
