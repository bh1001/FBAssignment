#Write a program to print list after removing even numbers.

# Create a list 'num' containing several integer values
num = [7, 8, 120, 25, 44, 20, 27]

# Use a list comprehension to create a new list 'num' that includes only the elements from the original list
# where the element is not divisible by 2 (i.e., not even)
num = [x for x in num if x % 2 != 0]

# Print the modified 'num' list, which contains only odd values
print(num)
