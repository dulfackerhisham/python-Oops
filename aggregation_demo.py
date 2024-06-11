class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)


class Address:
    
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state

    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state


add_1 = Address("calicut", 673306, "kerala")
cust_1 = Customer("hisham", "male", add_1)

cust_1.edit_profile("nidal", "quilandy", 673305, "kozhikode")

print(cust_1.address.pin)