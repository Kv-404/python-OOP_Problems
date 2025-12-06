class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")


# ----- Main Program -----
account = BankAccount("User", 1000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = float(input("Enter deposit amount: "))
        account.deposit(amt)

    elif choice == 2:
        amt = float(input("Enter withdrawal amount: "))
        account.withdraw(amt)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice!")
