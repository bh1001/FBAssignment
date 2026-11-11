#Write a program of having n number of elements in the list and find out even
#and odd elements in that list and then create two separate lists which will have
#even elements and other will have odd elements.


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in a if n % 2 == 0]
odds = [n for n in a if n % 2 != 0]

print(evens)  
print(odds)