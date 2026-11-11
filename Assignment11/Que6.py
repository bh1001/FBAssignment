#Python Program to Find the Union of two Lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

# Using the union() method
union_set = set(list1).union(set(list2))
union_list = list(union_set)
print(f"Union using .union(): {union_list}")

# Using the | operator (shortcut for union)
union_set_op = set(list1) | set(list2)
union_list_op = list(union_set_op)
print(f"Union using | operator: {union_list_op}")

# Output (order may vary as sets are unordered):
# Union using .union(): [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Union using | operator: [1, 2, 3, 4, 5, 6, 7, 8, 9]
