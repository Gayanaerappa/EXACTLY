Balance = 50000
correct_pin = "1234"
attempts = 3
transactions = [] # store history 
print("----------Welcom to the ATM----------")
while  attempts > 0:
    user_pin = input("Enter the password:")
    if user_pin == correct_pin:
        print("Login successful")
        while True:
            print("\n 1. check balance")
            print("2. deposite Money")
            print("3. Withdraw Money")
            print("4.Mini Statement")
            print("5.Exit")
            choice = input("Enter the Choice:")
            if choice == "1":
                print("Your account balance is",Balance) 
            elif choice == "2":
                amount = int(input("Enter the amount to deposite:"))
                Balance = Balance + amount
                transactions.append(f"deposited: {amount}")
                print("Deposite Successful")
            elif choice == "3":
                amount = int(input("Enter the amount to Withdraw:"))  
                if amount <=Balance:
                    Balance = Balance - amount
                    transactions.append(f"Withdraw:{amount}")
                    print("Collect your cash")
                else:
                    print("insufficient fount") 
            elif choice == "4":
                print("\n Mini statement") 
                if len(transactions)==0:
                    print("No Transaction Yet.")  
                else:
                    for t in transactions:
                        print(t)
                print("Current Balance",Balance)  
            elif choice == "5":
                print("Thank you for usning ATM")  
                break
            else:
                print("Invaild choice")    
    else:
        attempts = attempts-1 
        print("Wrong Pin")  
        print("attempts left:",attempts)    
if attempts == 0:
    print("\n card Blocked! too much Wrong attempts")              





     

    
