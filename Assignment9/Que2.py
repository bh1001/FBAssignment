# Python program to check Armstrong number using recursion

def power_sum(num, power):
    """Recursive function to calculate the sum of digits raised to the given power."""
    if num == 0:
        return 0
    else:
        return (num % 10) ** power + power_sum(num // 10, power)
def is_armstrong(num):
    """Function to check if a number is Armstrong using recursion."""
    digits = len(str(num))
    result = power_sum(num, digits)
    return result == num

# Example usage
number = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")