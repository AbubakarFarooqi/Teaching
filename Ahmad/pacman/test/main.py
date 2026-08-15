class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # PRIVATE
 
    def withdraw(self, amount):
        if amount > self.__balance:
            return   # rule ENFORCED
        self.__balance -= amount
 
    def get_balance(self):
        return self.__balance
 
acc = BankAccount("Ali", 10000)
acc.__balance = 1001  # attack FAILS
print(acc.__balance)
# print(acc.get_balance())  # 10000  ✓
