#Python Program to Sort the List According to the Second Element in Sublist

original_list = [['jack', 50], ['antony', 20], ['jones', 87], ['gary', 70]]

# Sort the list based on the second element of each sublist
sorted_list = sorted(original_list, key=lambda x: x[1])

print("Original list:", original_list)
print("Sorted list:", sorted_list)
