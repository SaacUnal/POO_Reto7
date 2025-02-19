import restaurant.restaurant

if __name__ == "__main__":
  # Elements
  nonAlcoholicBeverage = NonAlcoholicBeverage("Gazimba", 3000, ["cocaina", "azucar"], 500)
  appetizer = Appetizer("Salchichon", 2500, ["perro", "sal"])
  mainCourse = MainCourse("Carne", 50000, ["gato", "sal", "pimienta recien molida"])
  veganMenu = VeganMenu("Hamburguesa", 100000000, ["garbanzo", "quimicos"])
  cocktail = Cocktail("tequila", 45000, ["alcohol", "diversion :)"], 600)
  pastries = Pastries("galleta", 3000, ["harina", "azucar", "otras cosas"])
  iceCreamDessert = IceCreamDessert("banana split", 7500,["banana", "split", "helado"])
  fruitSalad = FruitSalad("Ensalada", 15000, ["frutas", "queso"])
  fastFood = FastFood("Pizza", 3000, ["PIÑA", "queso"])
  kidsMenu = KidsMenu("nuggets", 3000, ["pollo", "microplasticos"])

  # Order
  order = Order([appetizer, nonAlcoholicBeverage])
  order.add_item(cocktail)
  order.add_item(mainCourse)
  print(order.__str__())
  print(order.total_bill())

  # Pay
  payCard = Card("1234567890123456", 123, 50)
  payCash = Cash(100000)
  payCard.pay(order.total_bill())
  payCash.pay(order.total_bill())