"""
Enter the 2 numbers as user input 
ask the user to enter the operation they want to perform
Add, Subtract, Multiply, Divide
Then perform the operation and print the result
"""
# Simple Calculator
# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
# Perform the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."
# Print the result
print("The result is:", result)
# This is a simple calculator program that takes two numbers and an operation as input from the user.
