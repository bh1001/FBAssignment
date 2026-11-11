#Accept a number from user and check if this element is present in the list or
#not. Also tell how many times it is present in the list.

l = eval(input("Enter list: "))
n = int(input("Enter number to search: "))

if n in l:
    print(n, "found at index", l.index(n))
else :
    print(n, "not found in list")