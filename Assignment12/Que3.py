#Python Program to Detect if Two Strings are Anagrams

def is_anagram_sorted(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the length is the same
    if len(str1) != len(str2):
        return False
        
    # Sort the strings and compare them
    return sorted(str1) == sorted(str2)

# Example Usage:
s1 = "Listen"
s2 = "Silent"
if is_anagram_sorted(s1, s2):
    print(f"'{s1}' and '{s2}' are anagrams.")
else:
    print(f"'{s1}' and '{s2}' are not anagrams.")

# Example with non-anagrams:
s3 = "Hello"
s4 = "World"
if is_anagram_sorted(s3, s4):
    print(f"'{s3}' and '{s4}' are anagrams.")
else:
    print(f"'{s3}' and '{s4}' are not anagrams.")
