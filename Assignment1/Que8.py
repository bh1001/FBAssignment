#Write a program to convert days into years, weeks and days.

days=int(input("enter number of days"))

years=days//365
weeks=(days%365)//7
dayes=days-(365*years)-(7*weeks)

print('years'+str(years))
print('weeks'+str(weeks))
print('dayes'+str(dayes))