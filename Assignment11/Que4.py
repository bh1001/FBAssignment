#Python Program to Find the Second Largest Number in a List Using Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    # Outer loop for passes
    for i in range(n):
        # Inner loop to compare adjacent elements
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_second_largest(numbers):
    # Handle edge cases where the list has fewer than 2 elements or all elements are identical
    if len(set(numbers)) < 2:
        return "Not enough unique elements for a second largest number"
    
    # Sort the list using the custom bubble sort function
    sorted_numbers = bubble_sort(numbers)
    
    # The second largest number is the second element from the end
    return sorted_numbers[-2]

# Example usage:
my_list = [12, 34, 7, 23, 32, 56, 94]
second_largest = find_second_largest(my_list)
print(f"The second largest number in the list is: {second_largest}")

# Example with duplicates:
list_with_duplicates = [4, 10, 10, 6, 8]
second_largest_dup = find_second_largest(list_with_duplicates)
print(f"The second largest number in the list with duplicates is: {second_largest_dup}")
