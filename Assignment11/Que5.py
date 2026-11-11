#Python Program to Sort a List According to the Length of the Elements within the list.
original_list = ["apple", "banana", "kiwi", "orange", "grapefruit"]

# Sort by length in ascending order
sorted_list_asc = sorted(original_list, key=len)
print(f"Ascending order: {sorted_list_asc}")

# Sort by length in descending order
sorted_list_desc = sorted(original_list, key=len, reverse=True)
print(f"Descending order: {sorted_list_desc}")
