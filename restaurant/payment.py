class PaymentMethod:
  def pay(self, amount):
    raise NotImplementedError

class Card(PaymentMethod):
  def __init__(self, number, cvv, funds):
    self.__number = number
    self.__cvv = cvv
    self.__funds = funds 

  def get_number(self):
    return self.__number
  
  def get_funds(self):
    return self.__funds
  
  def pay(self, amount):
    funds = self.get_funds()
    if funds >= amount:
      print(f"Paying {amount} with card ending in: ***{self.get_number()[-4:]}")
    else:
      print(f"Insufficient funds. Amount needed: {amount - funds}")

class Cash(PaymentMethod):
  def __init__(self, delivered_amount):
    self.__delivered_amount = delivered_amount

  def get_delivered_amount(self):
    return self.__delivered_amount
  
  def pay(self, amount):
    delivered_amount = self.get_delivered_amount()
    if delivered_amount >= amount:
      print(f"Payment successfull. Change: {delivered_amount - amount}")
    else:
      print(f"Insufficient cash. Amount needed: {amount - delivered_amount}")
