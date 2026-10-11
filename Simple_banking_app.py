
balance = 0
def check_balance():
    print(f"Your Current Balance is {balance}")
    print("=" * 100)

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount

    else:
        print("Cannot deposit Negative or 0 Amount")
        print("=" * 100)

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Cannot withdraw Negative or 0 Amount")
        print("=" * 100)

    elif amount > balance:
        print("Cannot withdraw Amount greater than Balance")
        print("=" * 100)

    else:
        balance -= amount

if __name__ == "__main__":

    print("=" * 100)
    print("Welcome to the ABC Banking App")
    print("=" * 100)
    while True:

        print("1 . Check Your Balance")
        print("2 . Deposite an Amount")
        print("3 . Withdraw an Amount")
        print("4 . Quit")
        choice = input("Enter your choice(1-4) : ")
        print("=" * 100)

        if choice == "1":
            check_balance()
        elif choice == "2":
            amt = int(input("Enter your Amount to Deposit: "))
            deposit(amt)
            print(f"Amount deposited {amt} Successfully")

        elif choice == "3":
            amt = int(input("Enter your Amount to Withdraw: "))
            withdraw(amt)
            print(f"Amount withdraw {amt} Successfully")

        elif choice == "4":
            break

        else:
            print("Invalid Choice !!! Re-Try Again")
            print("=" * 100)


    print()
    print("Thank You for Banking ")
