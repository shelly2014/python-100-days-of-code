# Use Docstrings for print
# Add option to exit the calculator

from art_calc import logo

def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    continue_calc = True

    num1 = float(input("What's the first number?: "))
    while(continue_calc):
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))

        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        user_choice = input(f"""
Type 'y' to continue calculating with {result}
     'c' to clear and start a new calculation
     'n' to exit the calculator\n""").lower()
        if user_choice == 'n':
            continue_calc = False
        elif user_choice == 'c':
            calculator()
        else: 
            num1 = result

calculator()