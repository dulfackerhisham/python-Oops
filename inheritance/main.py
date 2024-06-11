class User:

    def login(self):
        print("Login")

    def register(self):
        print('Register')

class Student(User):

    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")

    
std_1 = Student()

std_1.enroll()
std_1.review()
std_1.login()
std_1.register()