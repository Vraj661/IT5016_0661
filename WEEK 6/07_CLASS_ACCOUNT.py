class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0: 
            self.__balance += amount
            print(f"${amount} deposited ")
        else:
            print("Deposit amount must be positive")
        
    def withdraw(self, amount):
        if  0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn ")
        else:
            print("Withdrawal amount must be positive and not exceed the balance")
            
Account = Account("James", 100)
print(Account.owner)
# print(Account.__balance)

Account.deposit(50)
print(Account.get_balance())
Account.withdraw(75)
print(Account.get_balance())

