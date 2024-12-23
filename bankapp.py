def createAccount():
    AcN=int(input("Enter Account Number: "))
    if AcN in bank:
        print("Account number already exist.Please try again.")
        return 
    name=input("Enter name of the Accountant: ")
    cont=int(input("Enter contact Number: "))
    balance=float(input("enter initial amount: "))
    bank[AcN]={"Name":name,"Contact":cont,"bal":balance}
    print("Account created Successfully!")
def deposit():
    acc_num=int(input("Enter your account number: "))
    if acc_num not in bank:
        print("Account not Found!")
        return
    try:
        amount=float(input("Enter amount to diposit: "))
        if amount<=0:
            print("Amount must be greater than zero")
        else:
            bank[acc_num]["bal"]+=amount
            print(f"successfully deposited Rs {amount:.2f}")
    except ValueError:
        print("Invalid input!Enter a valid amount to deposit")
def withdraw():
    acc_num=int(input("Enter account number: "))
    if acc_num not in bank:
        print("Account not found!")
        return 
    try:
        amount=float(input("Enter amount to withdraw: "))
        if amount<=0:
            print("Amount must be greater then zero")
        elif amount<=bank[acc_num]["bal"]:
            bank[acc_num]["bal"]-=amount
            print(f"Successfully withdraw Rs {amount:.2f}")
        else:
            print("Insufficient balance!")
    except ValueError:
        print("Invalid input.Enter a valid amount.")
def checkbalance():
    acc_num=int(input("Enter account number: "))
    if acc_num not in bank:
        print("Account not found!")
        return 
    print(f"Your current balance is Rs {bank[acc_num]['bal']:.2f}")
def displayDetails():
    acc_num=int(input("Enter account number: "))
    if acc_num not in bank:
        print("Account not found!")
        return 
    print("Account Details:")
    print(f"Name: {bank[acc_num]['Name']}")
    print(f"Contact: {bank[acc_num]['Contact']}")
    print(f"Balance: Rs {bank[acc_num]['bal']:.2f}")


print("========Menu========")
print("1.Create Account")
print("2.Deposit")
print("3.WithDraw")
print("4.check Balance")
print("5.Display Details")
print("6.Exit")
print("=====================")
bank={}
while True:
    try:
        ch=int(input("Enter your choice: "))
        if ch==1:
            createAccount()
        elif ch==2:
            deposit()
        elif ch==3:
            withdraw()
        elif ch==4:
            checkbalance()
        elif ch==5:
            displayDetails()
        elif ch==6:
            print("Thank you.Have a great day!")
            break
        else:
            print("Invalid choice.Please try again!")
    except ValueError:
        print("Invalid input!please enter a valid number.")
