class Account:

    def __init__(self, _id: int, name: str, balance=0):
        self.id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount) -> str or int:
        if amount <= self.balance:
            self.balance -= amount
            return self.balance

        return f'Amount exceeded balance'

    def info(self):
        return f'User {self.name} with account {self.id} has {self.balance} balance'


account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
