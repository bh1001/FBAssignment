#Python Program to Put Even and Odd elements of a List into two Different Lists

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Separate even numbers: condition is met if remainder is 0 when divided by 2
even_list = [num for num in original_list if num % 2 == 0]

# Separate odd numbers: condition is met if remainder is not 0
odd_list = [num for num in original_list if num % 2 != 0]

print("Original list:", original_list)
print("Even numbers list:", even_list)
print("Odd numbers list:", odd_list)
