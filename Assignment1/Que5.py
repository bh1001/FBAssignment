#Write a program to enter P, T, R and calculate Compound Interest.


p=int(input('enter principal'))
r=int(input('enter rate'))
t=int(input('enter time'))

amount=p*(pow((1+r/100),t))

ci=amount-p

print("compound interest is:", ci)

