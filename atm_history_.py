
import random
from datetime import datetime

class Account:
    depositFrequency = 4
    transactionMax = 40000

    def __init__(self, id, balance=0, withdrawalDailyMax=50000,
                 withdrawalFrequency=3, withdrwalTransactionMax=20000,
                 depoDailyMax=150000, depositFrequency=4, depoTransactionMax=40000):
        self.id = id
        self.balance = balance
        self.withdrawalDailyMax = withdrawalDailyMax
        self.withdrawalFrequency = withdrawalFrequency
        self.withdrwalTransactionMax = withdrwalTransactionMax
        self.depoDailyMax = depoDailyMax
        self.depositFrequency = depositFrequency
        self.depoTransactionMax = depoTransactionMax
        self.history = []

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def getWithdrawalFrequency(self):
        return self.withdrawalFrequency

    def getWithdrwalTransactionMax(self):
        return self.withdrwalTransactionMax

    def getWithdrawalDailyMax(self):
        return self.withdrawalDailyMax

    def getDepoDailyMax(self):
        return self.depoDailyMax

    def getDepositFrequency(self):
        return self.depositFrequency

    def getDepoTransactionMax(self):
        return self.depoTransactionMax

    def _stamp(self, action, amount=0.0):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append((ts, action, amount, self.balance))

    def withdraw(self, amount):  # withdraw
        self.balance -= amount
        self._stamp("WITHDRAW", amount)

    def deposit(self, amount):  # deposit
        self.balance += amount
        self._stamp("DEPOSIT", amount)

    def record_balance_check(self):  # balance check
        self._stamp("BALANCE_CHECK", 0.0)

    def format_history(self):  # history
        if not self.history:
            return "No transaction history available in this session."
        lines = ["\n--- Transaction History (most recent last) ---"]
        for ts, action, amount, bal in self.history:
            if action in ("DEPOSIT", "WITHDRAW"):
                lines.append(f"{ts}  {action:<14}  amount={amount}  balance={bal}")
            else:
                lines.append(f"{ts}  {action:<14}  balance={bal}")
        return "\n".join(lines)


def main():
    accounts = []
    for i in range(1000, 10000):
        account = Account(i, 0)
        accounts.append(account)

    while True:
        try:
            id_input = input("\n Please Enter Your account pin: ")
            id = int(id_input)
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")
            continue

        while id < 1000 or id > 9999:
            try:
                id = int(input("\nInvalid Pin.. Re-enter your Pin please: "))
            except ValueError:
                print("Invalid input. Please enter a 4-digit number.")
                continue

        accountObj = None
        for acc in accounts:
            if acc.getId() == id:
                accountObj = acc
                break

        if accountObj is None:
            print("Account not found. Please try again.")
            continue

        while True:
            print("\n1 - Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Quit \t 5 - View History ")

            try:
                selection = int(input("\nEnter your selection: "))
            except ValueError:
                print("\nThat's an invalid choice.")
                continue

            if selection == 1:
                print("Your balance is: " + str(accountObj.getBalance()) + " ")
                accountObj.record_balance_check()

            elif selection == 2:
                print("Your balance is: " + str(accountObj.getBalance()))
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
                    accountObj.withdraw(amt)
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
                else:
                    print("\nYour balance is less than the withdrawal amount: " + str(accountObj.getBalance()) + " \n")
                    print("\nPlease make a deposit.")

            elif selection == 3:
                print("Your balance is: " + str(accountObj.getBalance()) + " ")
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

                accountObj.deposit(amt)
                print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")

            elif selection == 4:
                check = input("Are you sure you want to quit? Yes or No: ").strip().lower()
                if check == "yes":
                    print("\nYour transaction is complete")
                    print("Transaction number: ", random.randint(10000, 1000000))
                    print("Thanks for choosing us as your bank")
                    break
                else:
                    print("Returning to menu.")

            elif selection == 5:
                print(accountObj.format_history())

            else:
                print("\nThat's an invalid choice.")

if __name__ == "__main__":
    main()
