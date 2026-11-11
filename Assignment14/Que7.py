#Given two sets of numbers, write a Python program to find the missing
#numbers in the second set as compared to the first and vice versa.Use the Python set.

# Define the two initial sets of numbers
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {2, 4, 6, 8, 10, 12, 14, 16}

# Find numbers in set1 that are not present in set2
# The difference() method or '-' operator returns a new set with elements present in the first set but not in the second.
missing_in_set2 = set1.difference(set2) 
# Alternatively: missing_in_set2 = set1 - set2

# Find numbers in set2 that are not present in set1
missing_in_set1 = set2.difference(set1)
# Alternatively: missing_in_set1 = set2 - set1

# Print the results
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print("-" * 30)
print(f"Numbers in Set 1 missing from Set 2: {missing_in_set2}")
print(f"Numbers in Set 2 missing from Set 1: {missing_in_set1}")

# Example of symmetric difference (numbers unique to either set)
# The symmetric_difference() method or '^' operator returns all elements that are in exactly one of the sets.
# symmetric_diff = set1.symmetric_difference(set2)
# print(f"Symmetric difference (numbers unique to either set): {symmetric_diff}")
