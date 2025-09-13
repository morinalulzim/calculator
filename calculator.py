# Simple Calculator in Python - Version 1.2.0
# Learning Goals: Variables, Input, Output, Basic Arithmetic

# Greet the user
print("Simple Calculator")
print("Welcome! This calculator can perform addition, subtraction, multiplication, division, exponentiation, modulus, and floor division.")

# Function to safely get a number from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

while True:
    # Get the first number from the user
    x = get_number("Enter first number: ")

    # Ask the user which operations to perform
    operation = input("Choose operation (+, -, *, /, ^, %, //): ")

    # Get the second number from the user
    y = get_number("Enter second number: ")

    # Then use conditional statements to perform the chosen operation
    if operation == '+':
        # Perform addition and display the result
        print("Sum is: ", x + y)
    elif operation == '-':
        # Perform subtraction and display the result
        print("Difference is: ", x - y)
    elif operation == '*':
        # Perform multiplication and display the result
        print("Product is: ", x * y)
    elif operation == '/':
        # Perform division with zero-check and display the result
        if y != 0:
            print("Quotient is: ", x / y)
        else:
            print("Division with zero is not allowed.")
    # Extended arithmetic operations: exponentiation, modulus, floor division
    elif operation == '^':
        # Perform exponentiation and display the result
        print("Exponentiation (x^y) is: ", x ** y)
    elif operation == '%':
        # Perform modulus operation and display the result
        if y != 0:
            print("Modulus (x % y) is: ", x % y)
        else:
            print("Modulus with zero is not allowed.")
    elif operation == '//':
        # Perform floor division with zero-check and display the result
        if y != 0:
            print("Floor Division (x // y) is: ", x // y)
        else:
            print("Floor division with zero is not allowed.")
    else:
        # Handle invalid operation input
        print("Invalid operation selected.")

    continue_calculating = input("Do you want to perform another calculation? (y/n): ")
    if continue_calculating.lower() != 'y':
        print("Thank you for using the calculator. Goodbye!")
        break