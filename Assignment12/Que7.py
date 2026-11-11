#Python Program to Take in a String and Replace Every Blank Space
#with Hyphen

# Prompt the user for input
input_string = input("Enter a string: ")

# Replace all occurrences of ' ' (space) with '-' (hyphen)
# The replace() method is a built-in string method that returns a copy
# of the string with all occurrences of the substring old replaced by new.
modified_string = input_string.replace(' ', '-')

# Display the original and modified strings
print(f"Original string: {input_string}")
print(f"Modified string: {modified_string}")
