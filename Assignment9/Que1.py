#Write a program to find sum of following series using recursive functions:

# 1! + 2! + 3! + 4! +..... + n!
#Note : For fact and sum two recursive functions

#recursive function to calculate the sum of the series.
def SeriesSum(n):
   # Base case
   if n==0:
      return 0
   #store each value in a variable m
   m= (n*(n+1)*(n+2))
   #making a recursive call
   return m + SeriesSum(n-1)
num=5
print("The sum of the series is:", SeriesSum(num));