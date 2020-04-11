class Account():

  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    newBalance = self.balance + amount
    print("Deposit successful. Your new balance is: {}".format(newBalance))

  def withdraw (self, amount):
    if amount <= self.balance:
      result = self.balance - amount
      print("Withdrawal successful. Your new balance is: {}".format(result))
    else: 
      print ("The amount exceeds the available balance")

  def __str__(self):
    return "Account owner: " + self.owner + "\nAccount balance: " + str(self.balance)

myAccount = Account("Stef", 547)
print(myAccount.__str__())

print(myAccount.deposit(100))
print(myAccount.withdraw(800))
