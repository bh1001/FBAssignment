#Python Program to Replace all Occurrences of ‘a’ with $ in a String


# declaring a string variable
str = "An apple A day keeps doctor Away."

# replacing character a with $ sign
str = str.replace('a', '$')
str = str.replace('a'.upper(),'$')
print("Modified string : ")
print(str)