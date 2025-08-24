# will gonna make a calculator that takes a function as input

def add(x, y):
    return x + y    

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):  
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator(func, x, y):
    return func(x, y)

# Example usage
if __name__ == "__main__":
    print("Addition:", calculator(add, 5, 3))
    print("Subtraction:", calculator(subtract, 5, 3))
    print("Multiplication:", calculator(multiply, 5, 3))
    print("Division:", calculator(divide, 5, 3))
    print("Division by zero:", calculator(divide, 5, 0))

