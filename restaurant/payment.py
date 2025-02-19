class PaymentMethod:
  def __init__(self):
    pass

  def pay(self, amount):
    raise NotImplementedError

class Card(PaymentMethod):
  def __init__(self, numero, cvv, funds):
    super().__init__()
    self.numero = numero
    self.cvv = cvv

    '''
    Esto seria si la clase fuera usada por el banco y el restaurante solo la
    llama, en otro caso no deberia saber cuanto saldo tiene.
    '''

    self.funds = funds 

  def pay(self, amount):
    if self.funds >= amount:
      print(f"Paying {amount} with card ending in: ***{self.numero[-4:]}")
    else:
      print(f"Insufficient funds. Amount needed: {amount - self.funds}")

class Cash(PaymentMethod):
  def __init__(self, delivered_amount):
    super().__init__()
    self.delivered_amount = delivered_amount

  def pay(self, amount):
    if self.delivered_amount >= amount:
      print(f"Payment successfull. Change: {self.delivered_amount - amount}")
    else:
      print(f"Insufficient cash. Amount needed: {amount - self.delivered_amount}")
