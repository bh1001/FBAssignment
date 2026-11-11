#Write a program to calculate the percentage of student based on marks of any 5 subjects.
print("Enter marks of five subjects:")
S1=float(input())
S2=float(input())
S3=float(input())
S4=float(input())
S5=float(input())

#Calculate total, average and percentage one by one
total = S1 + S2 + S3 + S4 + S5;
average = total/5.0;
percentage = (total / 500.0) * 100;

#Print the result
print("Total marks = ", total)
print("Average marks = ", average)
print("Percentage = ", percentage)