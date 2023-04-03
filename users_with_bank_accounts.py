class BankAccount:
    def __init__(self, interest=0.01, balance=0):
        self.interest = interest
        self.balance = balance
    def deposit(self, amount):
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
    def deposit(self, amount):
        self.checking.deposit(amount)
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


me = User("devin", "email@email.com")
me.deposit(100).display_account_info()

steve = User("steve", "steve@steve.steve")
steve.deposit(1000).transfer_money(200,me).display_account_info()
