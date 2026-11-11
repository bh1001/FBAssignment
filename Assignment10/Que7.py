#Write a program to create a new list from existing list which contains cube of
#each number of list.

# The original list of numbers
original_list = [1, 2, 3, 4, 5]

# Using a list comprehension to create a new list with cubes
# The syntax is [expression for item in iterable]
cubed_list = [num ** 3 for num in original_list]

# Print both lists to show the result
print("Original list:", original_list)
print("Cubed list:", cubed_list)
