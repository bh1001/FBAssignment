#Write a Program to input two angles from user and find third angle of the triangle
# Python Program to find Third Angle of Triangle if Two Angles Are Given
# get the value of two angles of triangle
Angle1 = int(input("Enter Angle 1 :--> "))
Angle2 = int(input("Enter Angle 2 :--> "))
Angle3 = 180 - (Angle1 + Angle2)               # sum of all the angles is 180
print("Third angle of the triangle :--> ", Angle3)