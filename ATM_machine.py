class Atm:
    
    def __init__(self, *args, **kwargs):
        self.pin = ""
        self.balance = 0

        self.menu()


    def menu(self):
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
        self.pin = input("Enter to set your PIN ")
        print("PIN set successfully")
        self.menu()

    def deposit(self):
        temp = input("Enter your PIN")
        if temp == self.pin:
            amount = int(input("Enter the amount "))
            self.balance += amount
        else:
            print("Invalid PIN")

    def withdraw(self):
        temp = input("Enter your PIN ")
        if temp == self.pin:
            amount = int(input("Enter the amount "))
            if amount < self.balance:
                self.balance -= amount
                print("Operation successfull ")
            else:
                print("Insufficient funds ")
        else:
            print("invalid PIN ")

    def check_balance(self):
        temp = input("Enter your PIN ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid PIN ")

sbi = Atm()
sbi.deposit()
sbi.withdraw()
sbi.check_balance()

