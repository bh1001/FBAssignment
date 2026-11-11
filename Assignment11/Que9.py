#Write a program to create three lists of numbers, their squares and cubes
# Initialize empty lists
numbers = []
squares = []
cubes = []

# Define the range of numbers (e.g., from 1 to 10, inclusive)
start = 1
end = 10

# Iterate through the range of numbers
for count in range(start, end + 1):
    numbers.append(count)
    squares.append(count**2)
    cubes.append(count**3)

# Print the resulting lists
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Cubes: {cubes}")
