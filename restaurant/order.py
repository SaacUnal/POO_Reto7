from menu import *

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
