#Write a Python program to find all the anagrams and group them together from a given list of #strings.

from collections import defaultdict

w = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Use defaultdict to group anagrams
a = defaultdict(list)
for word in w:
    s = ''.join(sorted(word))  # Sort each word to identify anagrams
    a[s].append(word)

# Convert defaultdict to a regular list of groups
res = list(a.values())
print(res)