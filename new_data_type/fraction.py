class Fraction:

    
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self,other):
        temp_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        temp_denominator = self.denominator * other.denominator
        
        return f"{temp_numerator}/{temp_denominator}"
    
    def __sub__(self,other):
        temp_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        temp_denominator = self.denominator * other.denominator
        
        return f"{temp_numerator}/{temp_denominator}"
    
    def __mul__(self,other):
        temp_numerator = self.numerator * other.numerator
        temp_denominator = self.denominator * other.denominator
        
        return f"{temp_numerator}/{temp_denominator}"
    
    def __truediv__(self,other):
        temp_numerator = self.numerator * other.denominator
        temp_denominator = self.denominator * other.numerator
        
        return f"{temp_numerator}/{temp_denominator}"

# x = Fraction(4, 5)
# print(type(x))

# p = [1,2,3, x]
# print(p)

"""trials"""

x = Fraction(3,4)
y = Fraction(5,6)
print(x)
print(y)

print("------------------------")
print(x + y)
print(x - y)
print(x * y)
print(x / y)