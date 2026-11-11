##Write a program to calculate area of circle 
import math
def calculate_are_circle(rad):
    area= 3.14*rad**2
    return area
rad =int(input("enter radious:"))
print("area of a circle:",calculate_are_circle(rad));
    