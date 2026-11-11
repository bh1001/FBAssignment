#Python Program to Multiply All the Items in a Dictionary
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result = 1

for value in my_dict.values():
    result *= value

print(f"The product of all items is: {result}")
