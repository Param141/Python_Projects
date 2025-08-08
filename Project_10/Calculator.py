import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}") # to see the whole calculation and not only the answer

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer # storing the answer to use it in the next calculation
        else:
            should_accumulate = False
            print("\n" * 20) #  starting a new line to clear the screen and start fresh not just appending to the previous calculations
            calculator() # recursively calling the calculator function to start a new calculation


calculator() # calling the calculator function to start the program
# This code implements a simple calculator that can perform basic arithmetic operations.
# It allows users to perform multiple calculations in a single session.

# basically we are using the logic that can  call the function through  a varible also in which its name is stored by passing parameters
# like operations["*"](4, 8) will call the multiply function and pass 4 and 8 as parameters
# and return the result of multiplication. 
# as operations["*"] is a function and we can call it like this.