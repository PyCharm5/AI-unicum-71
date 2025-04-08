class BankAccount:
    def __init__(self):
        self._balance = 500
        self._withdraw_sum = 0

    @property
    def balance(self):
        return self._balance

    @property
    def withdraw(self):
        return self._withdraw_sum

    def deposit(self, amount):
        self._balance += int(amount)

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            self._withdraw_sum += amount
        else:
            print("Недостаточно средств.")

bank = BankAccount()
bank.deposit(500)
print(bank.balance)