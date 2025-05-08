class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Public attribute
        self._balance = balance  # "Private" attribute (by convention)
        self.__account_number = "12345"  # Name mangled attribute


account = BankAccount("John")
print(account.owner)  # Accessible: John
print(account._balance)  # Accessible but shouldn't be accessed directly: 0
# print(account.__account_number)  # AttributeError
print(account._BankAccount__account_number)
# Accessible through mangled name: 12345
