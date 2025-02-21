# Importing each module cause its easier writing in main - dont need to write something like menu.Appetizer
from restaurant.menu import *
from restaurant.order import Order
from restaurant.payment import *
from restaurant.queue import Queue

if __name__ == "__main__":
  # Elements - this could be a db
  nonAlcoholicBeverage = NonAlcoholicBeverage("Gazimba", 3000, ["cocaina", "azucar"], 500)
  appetizer = Appetizer("Salchichon", 2500, ["perro", "sal"])
  mainCourse = MainCourse("Carne", 50000, ["gato", "sal", "pimienta recien molida"])
  veganMainCourse = VeganMainCourse("Hamburguesa", 100000000, ["garbanzo", "quimicos"])
  cocktail = Cocktail("tequila", 45000, ["alcohol", "diversion :)"], 600)
  pastries = Pastries("galleta", 3000, ["harina", "azucar", "otras cosas"])
  dessert = Dessert("banana split", 7500,["banana", "split", "helado"])
  fruitSalad = FruitSalad("Ensalada", 15000, ["frutas", "queso"])
  fastFood = FastFood("Pizza", 3000, ["PIÑA", "queso"])
  kidsMenu = KidsMenu("nuggets", 3000, ["pollo", "microplasticos"])

  # Orders - this will be used by the waiter
  # For the sake of the customer you gotta use a FIFO 
  # but sometimes you need to modify the orders or a customer finish before another
  orders = Queue()
  orders.set(Order([appetizer, nonAlcoholicBeverage]))
  orders.set(Order([appetizer, pastries, dessert]))
  orders.set(Order([veganMainCourse, fruitSalad, kidsMenu]))
  orders.get(1).add_item(cocktail)
  orders.get(1).add_item(mainCourse)
  orders.get(1).remove_item(appetizer)
  print(orders)

  # Making them - this is what the chefs are going to see
  orders.get()
  orders.get(1)

  # Pay - this will be used at the cash register
  payCard = Card("1234567890123456", 123, 50)
  payCash = Cash(100000)
  payCard.pay(orders.remove(2).total_bill())
  payCash.pay(orders.remove().total_bill())

  print(orders)