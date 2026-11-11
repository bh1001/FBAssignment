#Write a program to calculate the m to the power n using recursion.

def power(m, n):
  """
  Calculates m to the power of n using recursion.

  Args:
    m: The base number.
    n: The exponent.

  Returns:
    The result of m raised to the power of n.
  """
  if n == 0:
    return 1
  else:
    return m * power(m, n - 1)

# Example Usage:
base = 2
exponent = 5
result = power(base, exponent)
print(f"{base} to the power of {exponent} is: {result}")

base = 3
exponent = 4
result = power(base, exponent)
print(f"{base} to the power of {exponent} is: {result}")
