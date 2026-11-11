#Python Program to Find the Intersection of Two Lists
list1 = [1, 2, 3, 4, 5, 3]
list2 = [4, 5, 6, 7, 8, 3]

# Convert lists to sets and find the intersection
intersection_set = set(list1) & set(list2)

# Convert the result back to a list (optional)
intersection_list = list(intersection_set)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Intersection: {intersection_list}")
