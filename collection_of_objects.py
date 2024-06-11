class Customer:

    
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"I am {self.name} and i am {self.age}")

c1 = Customer("hisham", 23)
c2 = Customer("fahim", 21)
c3 = Customer("aflu", 24)

L = [c1,c2,c3]

for i in L:
    # print(i.name, i.age)
    i.intro()