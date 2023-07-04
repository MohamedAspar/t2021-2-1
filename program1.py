class Calculate:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        if self.b !=0:
            return self.a / self.b
        else:
            return "error : division by zero is not allowed"


a= float(input("enter the first number(a)"))
b= float(input("enter the second number (b)"))
operation = input("enter the type of operation(add/subtract/multiply/divide):")

cal = Calculate(a,b)

if operation == "add":
    result = cal.add()
elif operation == "subtract":
    result = cal.subtract()
elif operation == "multiply":
    result = cal.multiply()
elif operation == "divide":
    result = cal.divide()
else:
    result = "Error: Invalid operation."

print("Result:", result)
