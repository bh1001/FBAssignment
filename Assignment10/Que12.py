#Write a program to create three lists of numbers, their squares
#and cubes#

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate squares
squares = [num ** 2 for num in numbers]

# Calculate cubes
cubes = [num ** 3 for num in numbers]

# Print the lists
print(&quot;Numbers:&quot;, numbers)
print(&quot;Squares:&quot;, squares)
print(&quot;Cubes:&quot;, cubes)