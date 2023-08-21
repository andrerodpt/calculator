from art import logo

#Add
def add(n1, n2):
    """Takes the input of two integers and return the sum"""
    return n1 + n2

#Subtract
def subtract(n1, n2):
    """Takes the input of two integers and return the subtraction"""
    return n1 - n2

#Multiply
def multiply(n1, n2):
    """Takes the input of two integers and return the multiplication"""
    return n1 * n2

#Divide
def divide(n1, n2):
    """Takes the input of two integers and return the division"""
    return n1 / n2

operations = {
    '+': add, 
    '-': subtract,
    '*': multiply,
    '/': divide,   
}

def calculator():
    print(logo)
    continue_calculation = True
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    while continue_calculation:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number? "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_continue_calculation = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation.: ")

        if user_continue_calculation == 'n':
            continue_calculation = False
            calculator()
        else:
            num1 = answer

calculator()