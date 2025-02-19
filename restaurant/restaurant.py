# Menu ------------------------------------------------------------------------

class MenuItem:
  def __init__(self, name: str, price: float, ingredients: list):
    self.name = name
    self.price = price
    self.ingredients = ingredients

  def total_price(self):
    return self.price
  
  def set_name(self, new_name):
    if new_name:
      self.name = new_name

  def get_name(self):
    return self.name
  
  def set_price(self, new_price):
    if new_price:
      self.price = new_price

  def get_price(self):
    return self.price
  
  def set_ingredients(self, new_ingredients):
    if new_ingredients:
      self.ingredients = new_ingredients

  def get_ingredients(self):
    return self.ingredients

# Items -----------------------------------------------------------------------

class NonAlcoholicBeverage(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list, volume: float):
    super().__init__(name, price, ingredients)
    self.volume = volume
  
  def set_volume(self, new_volume):
    if new_volume:
      self.volume = new_volume

  def get_volume(self):
    return self.volume

class Appetizer(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class MainCourse(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class VeganMenu(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class Cocktail(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list, volume: float):
    super().__init__(name, price, ingredients)
    self.volume = volume
  
  def set_volume(self, new_volume):
    if new_volume:
      self.volume = new_volume

  def get_volume(self):
    return self.volume

class Pastries(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class IceCreamDessert(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class FruitSalad(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class FastFood(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class KidsMenu(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

# Order -----------------------------------------------------------------------

class Order():
  def __init__(self, items: list):
    self.items = items
  
  def __str__(self):
    order = "Order: "
    for item in self.items:
      order += f"{item.name}, "
    return order

  def add_item(self, item: MenuItem):
    self.items.append(item)
  
  def total_bill(self):
     
    '''
    Si fuera un restaurante, las ordenes serian pequeñas por lo que 
    repetir ciclos no gastaria suficiente memoria como para ser un problema.
    '''

    # Discounts
    # First
    first = False
    for item in self.items:
      if isinstance(item, MainCourse):
        first = True
    
    if first:
      for item in self.items:
        if isinstance(item, NonAlcoholicBeverage):
          item.price *= 0.9

    # Total    
    total = 0
    for item in self.items:
      total += item.total_price()

# Payment ------------------------------------------------------------------------

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
