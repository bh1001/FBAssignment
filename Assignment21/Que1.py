try:
    # Taking input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Taking operator input
    operator = input("Enter operator (+, -, *, /): ")

    # Checking operator and performing calculation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2
    else:
        raise ValueError("Invalid Operator")

    print("Result:", result)

# Exception for invalid numbers
except ValueError as e:
    print("Error: Invalid number or operator entered.")

# Exception for division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# General exception (optional safety)
except Exception as e:
    print("Unexpected error:", e)