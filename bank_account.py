class BankAccount:
    def __init__(self, int_rate = 0.025, balance = 0):
        self.rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if self.account_balance - amount > 0:
            # print("OK to withdraw")
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
    def display_account_info(self):
        print("Balance:", self.account_balance)
        return self
    def yeild_interest(self):
        if self.account_balance > 0:
            amount=self.rate*self.account_balance
            self.account_balance += amount
            return self

account1 = BankAccount(balance = 500)
account2 = BankAccount(balance=300)

account1.deposit(50),account1.deposit(100),account1.deposit(50),account1.withdraw(100),account1.yeild_interest(),account1.display_account_info()
account2.deposit(100),account2.deposit(50),account2.withdraw(50),account2.withdraw(50),account2.withdraw(100),account2.withdraw(100),account2.yeild_interest(),account2.display_account_info()

