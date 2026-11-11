#Python Program to Count the Number of Vowels in a String

def count_vowels(input_string):
    """
    Counts the number of vowels (a, e, i, o, u) in a given string.
    """
    # Define the set of vowels for easy checking
    vowels = "aeiou"
    count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        # Convert character to lowercase to handle both uppercase and lowercase vowels
        if char.lower() in vowels:
            count += 1
            
    return count

# Example usage
text = "Hello World! This is a Python program."
num_vowels = count_vowels(text)

print(f"The string is: '{text}'")
print(f"The number of vowels is: {num_vowels}")
