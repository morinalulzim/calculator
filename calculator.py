# Simple Calculator in Python - Version 1.0
# Learning Goals: Variables, Input, Output, Basic Arithmetic

# Greet the user
print("Simple Calculator")
print("Welcome! This calculator can perform addition, subtraction, multiplication, division, exponentiation, modulus, and floor division.")

# Get two numbers from the user
x = float(input("Input the first number: "))
y = float(input("Input the second number: "))

# Ask the user which operations to perform
operation = input("Choose operation (+, -, *, /, ^, %, //): ")
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
    # Perform division and display the result
    if y != 0:
        print("Quotient is: ", x / y)
    else:
        print("Division with zero is not allowed.")
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
    # Perform floor division and display the result
    if y != 0:
        print("Floor Division (x // y) is: ", x // y)
    else:
        print("Floor division with zero is not allowed.")
else:
    print("Invalid operation selected.")

# End of the calculator program