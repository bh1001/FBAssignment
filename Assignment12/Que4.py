#Python Program to Form a New String where the First Character and
#the Last Character have been Exchanged

def swap_first_last(s):
    """
    Exchanges the first and last characters of a given string.

    Args:
        s: The input string.

    Returns:
        A new string with the first and last characters swapped.
    """
    if len(s) <= 1:
        return s
    
    # Slice the string to get the middle characters
    middle = s[1:-1]
    
    # Form the new string: last_char + middle + first_char
    new_string = s[-1] + middle + s[0]
    
    return new_string

# Example Usage:
original_string1 = "Python"
swapped_string1 = swap_first_last(original_string1)
print(f"Original: {original_string1}")
print(f"Swapped:  {swapped_string1}")
# Output:
# Original: Python
# Swapped:  nythoP

print("-" * 20)

original_string2 = "Hello World"
swapped_string2 = swap_first_last(original_string2)
print(f"Original: {original_string2}")
print(f"Swapped:  {swapped_string2}")
# Output:
# Original: Hello World
# Swapped:  dellO WorlH

print("-" * 20)

original_string3 = "a"
swapped_string3 = swap_first_last(original_string3)
print(f"Original: {original_string3}")
print(f"Swapped:  {swapped_string3}")
# Output:
# Original: a
# Swapped:  a
