# Absolute import = writing the whole path
# Relative import = one dot is the same folder, two dots is the parent folder
from .menu import *  

class Order():
  def __init__(self, items: list):
    self.__items = items

  def add_item(self, item: MenuItem):
    self.__items.append(item)
  
  def remove_item(self, item: MenuItem):
    self.__items.remove(item)

  def get_items(self):
    return self.__items

  def __str__(self): # I think it seems bad to put dunder's separate but idk
    order = "Order: "
    for item in self.get_items():
      order += f"{item}, "
    return order

  def item_discount(self, item):
    price = item.get_price() 
    match item:
      case isinstance(item, NonAlcoholicBeverage):
        price *= 0.9
        return price
      case isinstance(item, Pastrie):
        price *= 0.7
        return price
      case _:
        return price 
  
  def total_bill(self):
    total = 0
    for item in self.__items:
      item.set_price(self.item_discount(item))
      total += item.total_price()    
    return total
    
