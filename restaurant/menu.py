class MenuItem:
  def __init__(self, name: str, price: float, ingredients: list):
    self.__name = name
    self.__price = price
    self.__ingredients = ingredients
  
  def set_name(self, new_name):
    self.__name = new_name
  
  def get_name(self):
    return self.__name

  def __str__(self):
    return f"{self.get_name()}" # Cant put the atribute, must turn it to a str

  def set_price(self, new_price):
    self.__price = new_price

  def total_price(self):
    return self.__price
    
  def set_ingredients(self, new_ingredients):
    self.__ingredients = new_ingredients

  def get_ingredients(self):
    return self.__ingredients

# Items -----------------------------------------------------------------------

class NonAlcoholicBeverage(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list, volume: float):
    super().__init__(name, price, ingredients)
    self.__volume = volume
  
  def set_volume(self, new_volume):
    self.__volume = new_volume

  def get_volume(self):
    return self.__volume

class Appetizer(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class MainCourse(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class VeganMainCourse(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class Cocktail(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list, volume: float):
    super().__init__(name, price, ingredients)
    self.__volume = volume
  
  def set_volume(self, new_volume):
    self.__volume = new_volume

  def get_volume(self):
    return self.__volume

class Pastries(MenuItem):
  def __init__(self, name: str, price: float, ingredients: list):
    super().__init__(name, price, ingredients)

class Dessert(MenuItem):
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

# Combos -----------------------------------------------------------------------

class Combo(MenuItem):
  def __init__(self, name: str, price: float, items: list[MenuItem]):
    super().__init__(name, price, items)


