from art import *
import os


# Define the addition operation
def addition(n1, n2):
    return n1 + n2


# Define the subtraction operation
def subtraction(n1, n2):
    return n1 - n2


# Define the multiplication operation
def multiplication(n1, n2):
    return n1 * n2


# Define the division operation
def division(n1, n2):
    return n1 / n2


# Create a dictionary to store calculator operations
calculator_operations = {}

# Add mathematical operators as keys and corresponding functions as values to the dictionary
calculator_operations["+"] = addition
calculator_operations["-"] = subtraction
calculator_operations["*"] = multiplication
calculator_operations["/"] = division


def calculator():

    # Print the calculator logo
    print(logo)

    # Prompt the user to input the first number and convert it to an integer
    first_number = float(input("What is the first number?: "))

    # Set a flag to control the while loop for continuing calculations
    continue_calculation = True

    # Start a while loop to allow multiple calculations
    while continue_calculation:

        # Loop through the math operators and print each one for the user
        for operator in calculator_operations:
            print(operator)

        # Prompt the user to select a mathematical operation
        math_operator = input("Pick a math Operation: ")

        # Prompt the user to input the second number and convert it to an integer
        second_number = float(input("What is the second number?: "))

        # Retrieve the function corresponding to the chosen operator from the dictionary
        workout = calculator_operations[math_operator]

        # Pass the first and second numbers to the function and store the result in the 'answer' variable
        answer = workout(first_number, second_number)

        # Print the result of the current calculation
        print(f"{first_number} {math_operator} {second_number} = {answer}")

        # Prompt the user to decide whether to continue calculating with the current result
        continue_calc = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to not continue calculating: "
        )

        # If the user chooses to continue, set the current result as the new first number for the next calculation
        if continue_calc == "y":
            first_number = answer

        else:
            # Prompt the user to decide whether to start a new calculation or exit.
            new_calculation = input(
                "Type 'y' to start a new calculation, or type 'n' to exit. "
            )

            # If the user chooses to start a new calculation, set the flag to False and restart the calculator
            if new_calculation == "y":
                continue_calculation = False
                os.system("clear")  # Clears the current calculation
                calculator()  # Recursive call takes place to restart the calculator.
            else:
                # Set the flag to False and exits the program.
                continue_calculation = False


# Start the calculator program
calculator()
