#Write a program to remove all occurrences of a given element in the list.
def remove_all_occurrences_comprehension(data_list, element_to_remove):
    """
    Removes all occurrences of an element by creating a new list using list comprehension.
    """
    print(f"Original list: {data_list}")
    # Create a new list with elements that do not equal the element to remove
    new_list = [item for item in data_list if item != element_to_remove]
    print(f"New list after removal: {new_list}")
    return new_list

# Example usage:
my_list = [1, 2, 3, 4, 2, 5, 2]
# We assign the result to a new variable as the original list is unchanged
filtered_list = remove_all_occurrences_comprehension(my_list, 2)
# Output:
# Original list: [1, 2, 3, 4, 2, 5, 2]
# New list after removal: [1, 3, 4, 5]
