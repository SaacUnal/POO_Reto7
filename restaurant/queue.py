class Queue:
    def __init__(self):
        self.__items = []

    def __str__(self):
        orders = "Orders: \n"
        for order in self.__items:
            orders += f"{order}\n "
        return orders

    def set(self, element):
        self.__items.append(element)
        
    def get(self, index=0):
        if not self.empty():
            return self.__items[index]
        else:
            return None
        
    def remove(self, index=0):
        if not self.empty():
            return self.__items.pop(index)
        else:
            return None

    def empty(self):
        return len(self.__items) == 0 
