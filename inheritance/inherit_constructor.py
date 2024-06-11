class Phone:
    
    def __init__(self, price, brand, camera):
        print('inside phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('Buying phone')

    def return_phone(self):
        print('returning phone')

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    pass

s = SmartPhone(20000, "apple", 12)
print(s.brand)

s.buy()