class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'added {amount} to the balance')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return 'Withdrawal Accepted'
        else:
            return 'Not enough Funds !! '

    def __str__(self):
        return f'Owner : {self.owner} \nBalance : {self.balance}'


acc1 = Account('Luca', 1000)

#print(acc1.withdraw(5000))   # Funds Unavailable
#print(acc1.withdraw(200))    # 800
#print(acc1.deposit(500))     # 1300
#print(acc1)
