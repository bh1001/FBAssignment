#Write a program to remove duplicates from the list.
#original_list = [1, 2, 3, 4, 3, 2, 5, 6, 5]

# Convert the list to a set to remove duplicates, then convert back to a list
"""unique_list = list(set(original_list))

print(f"Original list: {original_list}")
print(f"List without duplicates (order not preserved): {unique_list}")"""


#using loop

a = [1, 2, 2, 3, 4, 4, 5]
u = []
for x in a:
    if x not in u:
        u.append(x)
print(u)
