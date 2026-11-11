##Write a program to calculate area of rectangle

def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle.
    """
    area = length * width
    return area

# Example usage:
rectangle_length = 10
rectangle_width = 5
area_result = calculate_rectangle_area(rectangle_length, rectangle_width)

print(f"The length of the rectangle is: {rectangle_length}")
print(f"The width of the rectangle is: {rectangle_width}")
print(f"The calculated area of the rectangle is: {area_result}")

