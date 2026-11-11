# Write a program to enter P, T, R and calculate simple Interest.

pr=int(input('enter principal'))
rate=int(input('enter rate'))
time=int(input('enter time'))

si=(pr*rate*time)/100

amount=pr+si
print('simple interest',si)
print('amount payable',amount)