"""this code will crash bcuz CHILD Class cant access Parent Class private members"""

class Phone:
    
    def __init__(self, price, brand, camera):
        print('inside phone constructor')
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def check(self):
        print(self.__price)

s = SmartPhone(20000, "apple", 12)
print(s.__price)
