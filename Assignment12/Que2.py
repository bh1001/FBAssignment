#Python Program to Remove the nth Index Character from a Non-Empty
#String

#Python program to remove nth index character from non-empty string
# declaring a string variable
str = "Geeksforgeeks is fun."

# index to remove character at
n = 8
print("Modified string after removing ", n, "th character ")
str=str.replace(str[n],"",1)
print(str)