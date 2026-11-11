#Write a program to find the second largest element in the list.
def find_second_largest_sorted(numbers):
    """
    Finds the second largest element by sorting the list.
    """
    # Remove duplicates to handle lists like [5, 5, 4] correctly
    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        return "List must have at least two unique elements"
    
    # Sort the unique numbers in ascending order
    unique_numbers.sort()
    
    # The second largest element is at the second-to-last position (index -2)
    return unique_numbers[-2]

# Example Usage:
my_list = [10, 5, 20, 8, 15, 20]
second_largest = find_second_largest_sorted(my_list)
print(f"The second largest element is: {second_largest}")
