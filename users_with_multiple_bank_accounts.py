# CODE BROKEN, MULTIPLE ACCOUNTS DOES NOT WORK

class BankAccount:
    def __init__(self, account_name, interest=0.01, balance=0):
        self.interest = interest
        self.balance = balance
        self.account_name = account_name
    def deposit(self, amount):
        print('depositing')
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance += self.balance*self.interest
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking = BankAccount(interest=0.01, balance=0)
        self.accounts = ["checking"]
    def deposit(self, account, amount):
        for account_name in self.accounts:
            if account.name == account:
                account.name.deposit(amount)
        # self.checking.deposit(amount)
        return self
    def withdraw(self, amount):
        self.checking.withdraw(amount)
        return self
    def display_account_info(self):
        self.checking.display_account_info()
        return self
    def yield_interest(self):
        self.checking.yield_interest()
        return self
    def transfer_money(self, amount, other_user):
        if self.checking.balance >= amount:
            other_user.checking.deposit(amount)
        self.checking.withdraw(amount)
        return self
    def create_bank_account(self, account="savings", interest=0.01, balance=0):
        setattr(self,account,BankAccount(interest,balance))
        self.accounts.append(account)
        return self
    def find_account(self, account):
        return getattr(self, account)


me = User("devin", "email@email.com")
me.create_bank_account("savings", .2, 100).deposit("savings", 100).display_account_info()
# me.checking.balance=100
# me.checking.deposit(100)

print("hello")