class Atm:
    
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        print(id(self))
        
        self.__menu()


    def get_pin(self):
        return f"this is the pin {self.__pin}"

    def set_pin(self,new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("PIN changed")
        else:
            print(f"{type(new_pin)} Not Allowed")



    def __menu(self):
        user_input = input("""
                        Hello,how would you like to proceed?
                        1. Enter 1 to create PIN
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. Enter 5 to exit
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.__pin = input("Enter to set your PIN ")
        print("PIN set successfully")
        # self.__menu()

    def deposit(self):
        temp = input("Enter your PIN")
        if temp == self.__pin:
            amount = int(input("Enter the amount "))
            self.__balance += amount
        else:
            print("Invalid PIN")

    def withdraw(self):
        temp = input("Enter your PIN ")
        if temp == self.__pin:
            amount = int(input("Enter the amount "))
            if amount < self.__balance:
                self.__balance -= amount
                print("Operation successfull ")
            else:
                print("Insufficient funds ")
        else:
            print("invalid PIN ")

    def check_balance(self):
        temp = input("Enter your PIN ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid PIN ")

idfc = Atm()
idfc.set_pin(98)
idfc.get_pin()   #get method is not working check it out

