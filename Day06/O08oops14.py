
class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("getter called.....")
        return self.__price

    @price.setter
    def price(self, val):
        print("setter called.....")
        if val < 0:
            raise ValueError ("Price cannot be less than zero")
        else:
            self.__price = val

    @price.deleter
    def price(self):
        print("deleter called......")
        self.__price = 0

pepsi = Product(150)
print(pepsi.price)
pepsi.price = 120
print(pepsi.price)
del pepsi.price
print(pepsi.price)