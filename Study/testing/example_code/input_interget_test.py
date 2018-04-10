import sys, traceback

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 // num2
    print("Result of division:", result)
except ValueError:
    print("Invalid input value")
    traceback.print_exc(file=sys.stdout)
except ZeroDivisionError:
    print("Cannot divide by zero")
    traceback.print_exc(file=sys.stdout)