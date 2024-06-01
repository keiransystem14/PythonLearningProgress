from art import *

# Print the calulator logo
print(logo)

# Empty dictionary
calculator_operations = {}

"""------------User Input--------------------"""

# User picks the first number
first_number = int(input("What is the first number?: "))

# Prompt the user to pick a mathmatical operation
math_operator = input("Pick an math Operation: ")

# User picls the second number
second_number = int(input("What is the second number?: "))

answer = calculator_operations[math_operator]

print(f"{first_number} {math_operator} {second_number} = {answer} ")

"""-----------------------------------------------------------------"""


# Add Operation
def addition(n1, n2):
    return n1 + n2


# Subtract Operation
def subtraction(n1, n2):
    return n1 - n2


# Multiply Operation
def multiplication(n1, n2):
    return n1 * n2


# Divide Operator
def division(n1, n2):
    return n1 / n2


# Add Mathmatical operators as key and function as the value into the dictionary. Pass both numbers the user choose inside the dictionary.
calculator_operations["+"] = addition(n1=first_number, n2=second_number)
calculator_operations["-"] = subtraction(n1=first_number, n2=second_number)
calculator_operations["*"] = multiplication(n1=first_number, n2=second_number)
calculator_operations["/"] = division(n1=first_number, n2=second_number)

# Loop through the math operators (+, -, *, /)
for operator in calculator_operations:
    print(operator)


# # Prompt user if they want to start a new calculation
# continue_calc = input(
#     "Type 'y' to continue calculating with total, or type 'n' to start a new calculation  "
# )
