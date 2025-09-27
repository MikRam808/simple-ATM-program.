# importing important modules
import random

class Account:
    depositFrequency = 4
    transactionMax = 40000

    # Construct an Account object.
    def __init__(self, id, balance=0, withdrawalDailyMax=50000,
                 withdrawalFrequency=3, withdrwalTransactionMax=20000,
                 depoDailyMax=150000, depositFrequency=4, depoTransactionMax=40000):
        self.id = id
        self.balance = balance
        # withdrawal
        self.withdrawalDailyMax = withdrawalDailyMax
        self.withdrawalFrequency = withdrawalFrequency
        self.withdrwalTransactionMax = withdrwalTransactionMax  # kept original attribute name to avoid breaking references
        # deposit
        self.depoDailyMax = depoDailyMax
        self.depositFrequency = depositFrequency
        self.depoTransactionMax = depoTransactionMax

    def getId(self):
        return self.id

    # a function to get balance
    def getBalance(self):
        return self.balance

    # getters for withdrawal
    def getWithdrawalFrequency(self):
        return self.withdrawalFrequency

    def getWithdrwalTransactionMax(self):
        return self.withdrwalTransactionMax

    def getWithdrawalDailyMax(self):
        return self.withdrawalDailyMax

    # getters for deposit
    def getDepoDailyMax(self):
        return self.depoDailyMax

    def getDepositFrequency(self):
        return self.depositFrequency

    def getDepoTransactionMax(self):
        return self.depoTransactionMax

    # a function to withdraw
    def withdraw(self, amount):
        # here if you withdraw your new balance changes
        self.balance -= amount

    # a function to deposit
    def deposit(self, amount):
        # deposit equals amount being deposited + existing balance
        self.balance += amount


def main():
    # Creating accounts (include 9999 as a valid id)
    accounts = []
    for i in range(1000, 10000):  # 10000 is exclusive; creates 1000..9999
        account = Account(i, 0)
        accounts.append(account)

    # ATM Processes
    while True:
        # Reading id from user which represents a secret pin for security
        try:
            id_input = input("\n Please Enter Your account pin: ")
            id = int(id_input)
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")
            continue

        # Loop till id is valid between 1000 and 9999
        while id < 1000 or id > 9999:
            try:
                id = int(input("\nInvalid Pin.. Re-enter your Pin please: "))
            except ValueError:
                print("Invalid input. Please enter a 4-digit number.")
                continue

        # find the account object
        accountObj = None
        for acc in accounts:
            if acc.getId() == id:
                accountObj = acc
                break

        # safety check (should not happen with the range above)
        if accountObj is None:
            print("Account not found. Please try again.")
            continue

        # while the pin is right (Id is pin here)
        while True:
            # Printing menu
            print("\n1 - Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Quit ")

            # Reading selection
            try:
                selection = int(input("\nEnter your selection: "))
            except ValueError:
                print("\nThat's an invalid choice.")
                continue

            # View Balance
            if selection == 1:
                print("Your balance is: " + str(accountObj.getBalance()) + " ")
            # Withdraw
            elif selection == 2:
                print("Your balance is: " + str(accountObj.getBalance()))
                # Reading amount
                try:
                    amt = float(input("\nPlease enter amount to withdraw: "))
                except ValueError:
                    print("Invalid amount.")
                    continue

                ver_withdraw = input(f"Is this the correct amount, Yes or No? {amt} ").strip().lower()
                if ver_withdraw != "yes":
                    print("Withdrawal cancelled.")
                    continue

                if amt <= 0:
                    print("Amount must be greater than 0.")
                    continue

                if amt <= accountObj.getBalance():
                    # Calling withdraw method
                    accountObj.withdraw(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
                else:
                    print("\nYour balance is less than the withdrawal amount: " + str(accountObj.getBalance()) + " \n")
                    print("\nPlease make a deposit.")
            # Deposit
            elif selection == 3:
                print("Your balance is: " + str(accountObj.getBalance()) + " ")
                # Reading amount
                try:
                    amt = float(input("\nEnter amount to deposit: "))
                except ValueError:
                    print("Invalid amount.")
                    continue

                ver_deposit = input(f"Is this the correct amount, Yes or No? {amt} ").strip().lower()
                if ver_deposit != "yes":
                    print("Deposit cancelled.")
                    continue

                if amt <= 0:
                    print("Amount must be greater than 0.")
                    continue

                # Calling deposit method
                accountObj.deposit(amt)
                # Printing updated balance
                print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
            # QUIT
            elif selection == 4:
                check = input("Are you sure you want to quit? Yes or No: ").strip().lower()
                if check == "yes":
                    print("\nYour transaction is complete")
                    print("Transaction number: ", random.randint(10000, 1000000))
                    print("Thanks for choosing us as your bank")
                    # Return to PIN prompt (end current session)
                    break
                else:
                    print("Returning to menu.")
            # Any other choice
            else:
                print("\nThat's an invalid choice.")

# call main
if __name__ == "__main__":
    main()