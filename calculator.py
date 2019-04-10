#Python program for simple Calculator for 2 inputs

class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2

print ("Hello, I can calculate given 2 numbers, please enter the numbers.")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
operation = input("Enter one of the operations (-, +, *, /): ")
C = calculator(num1, num2)

if operation == '+':
    print ("Result: ", C.add())
elif operation == '-':
    print ("Result: ", C.subtract())
elif operation == '*':
    print ("Result: ", C.multiply())
elif operation == '/':
    print ("Result: ", C.divide())
    exit()




