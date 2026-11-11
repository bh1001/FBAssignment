#Write a program to reverse a given number using recursive function.

# Reverse of a number using recursion
s = 0

def reverse(n):
    """
    Recursive function to calculate the reverse of a number.

    Parameters:
    - n (int): The input number.

    Returns:
    - int: The reversed number.
    """
    global s
    if n > 0:
        r = n % 10
        s = s * 10 + r
        n = n // 10
        reverse(n)
    return s

# Calling the reverse function
n = int(input("Enter a number: "))
x = reverse(n)
print("Reverse is %d" % x)