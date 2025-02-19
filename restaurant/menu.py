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

