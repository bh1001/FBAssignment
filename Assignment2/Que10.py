#Write a program to reverse three-digit number.

a=int(input('enter 3 digit number'))
r=a%10
r=r*10
a=a//10
r=r+a%10
r=r*10
r=r+a//10
print("reversed number is",r)