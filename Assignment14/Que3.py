#Write a Python program to find all the unique words and count the
#frequency of occurrence from a given list of strings. Use Python set data type.

# Define a function 'word_count' that takes a list of words as input and returns a dictionary of word counts.
def word_count(words):
    # Create a set 'word_set' to remove duplicate words from the input list.
    word_set = set(words)
    
    # Create an empty dictionary 'word_counts' to store word counts.
    word_counts = {}
    
    # Iterate over the unique words in 'word_set'.
    for word in word_set:
        # Count the occurrences of each word in the input list and store the count in 'word_counts'.
        word_counts[word] = words.count(word)
    
    # Return the 'word_counts' dictionary.
    return word_counts

# Create a list 'words' with words of various colors.
words = ['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']

# Call the 'word_count' function with the 'words' list and print the word counts.
print(word_count(words)) 
