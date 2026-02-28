class Account:
  def __init__(self,name,balance):
    self.name=name
    self.balance=balance
  def deposit(self,amount):
    self.amount=amount
    self.balance+=self.amount
    print(f"Rs.{self.amount} deposited your current balance is Rs.{self.balance}")
  def withdraw(self,amount):
    self.amount=amount
    if self.amount>self.balance:
      print("insufficient balance!")
    else:
      self.balance-=amount
      print(f"Rs.{amount} withdraw. Your account balance is Rs.{self.balance}")
    def balance_alert(self):
      if self.balance<500:
        print("alert: low balance! (below Rs. 500)")
      else:
        print("balanc is sufficient")
customer1=Account("Viknaya",700)

customer1.withdraw(300)
customer1.deposit(200)
