#Write a Python program to find the two numbers whose product is
#maximum among all the pairs in a given list of numbers. Use the Python set.

def find_max_product_pair(numbers_list):
    """
    Finds the two numbers whose product is maximum among all pairs in a given list.
    Uses a set to handle unique numbers.
    """
    # Convert the list to a set to efficiently work with unique numbers
    nums_set = set(numbers_list)

    # Handle edge case for lists with fewer than two unique numbers
    if len(nums_set) < 2:
        return None, None, "Not enough unique numbers for a pair"

    # Initialize max product and the pair of numbers
    max_product = float('-inf')
    max_num1 = None
    max_num2 = None

    # Iterate over all unique number pairs in the set
    for n1 in nums_set:
        for n2 in nums_set:
            # Ensure the numbers are distinct and their product is greater than the current max
            if n1 != n2 and n1 * n2 > max_product:
                max_product = n1 * n2
                max_num1 = n1
                max_num2 = n2

    return max_num1, max_num2, max_product

# Example Usage:
nums1 = [2, 5, 8, 7, 4, 3, 1, 9, 10, 1]
num1, num2, product = find_max_product_pair(nums1)
print(f"Original list: {nums1}")
print(f"Numbers with maximum product: ({num1}, {num2}), Product: {product}")

print("-" * 30)

nums2 = [-4, -10, 1, 2, 3, 4]
num3, num4, product2 = find_max_product_pair(nums2)
print(f"Original list: {nums2}")
print(f"Numbers with maximum product: ({num3}, {num4}), Product: {product2}")

print("-" * 30)

nums3 = [5, 5, 5, 5]
num5, num6, product3 = find_max_product_pair(nums3)
print(f"Original list: {nums3}")
print(f"Result: {product3}")
