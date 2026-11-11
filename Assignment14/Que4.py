#Write a Python program that finds all pairs of elements in a list whose sum is equal to a given #value.
lst = [1, 5, 3, 7, 9]
K = 12
result = []
seen = set()

for num in lst:
    complement = K - num
    if complement in seen:
        result.append((num, complement))
    seen.add(num)

print(result)