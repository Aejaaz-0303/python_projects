class Calculator:
    def __inti__(self):
        self.a=""
        self.b=""
    def display (self):
        print("Plese enter the numbers below")
        print("The Addition of given numbers are: " , (self.a + self.b))
        print("The Subtraction of given numbers are: " , (self.a - self.b))
        print("The Multiplication of given numbers are: " ,(self.a * self.b))
        print("The Division of given numbers are: " , (self.a / self.b))

Calc = Calculator()

Calc.a = int (input("Enter the numeber A: "))
Calc.b = int (input("Enter the numeber B: "))

Calc.display()