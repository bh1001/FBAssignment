#Write a program to reverse a number using recursion.

def rev_num(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(rev_num(n // 10)))

n = 987654
print(rev_num(n))