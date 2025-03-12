# Basic Calculator Program

'''Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.'''

try:
 num1 = float(input("Enter a first number: "))
 num2 = float(input("Enter a  second number: "))
 operation = input(" Enter a mathematical operation: (addition(+), subtraction(-), multiplication(*), or division(/): ")
 print(" ")
except ValueError:
 print("Invalid number, please try again: ")
 
# Addition
if operation == "+":
    print(f"Addition of {num1} and {num2} is: {num1+num2}")

# Subtraction    
elif operation == "-":
    print(f"Subtraction of {num1} and {num2} is: {num1-num2}")   

# Multiplication    
elif operation == "*":
    print(f"Multiplication of {num1} and {num2} is: {num1*num2}")   
       
# Division    
elif operation == "/":
    print(f"Division of {num1} and {num2} is: {num1/num2}")  
    
else:
    pass           