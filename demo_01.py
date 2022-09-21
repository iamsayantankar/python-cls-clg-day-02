# Q1. Write a program to print the Even numbers. The range must be given by the user.

n = int(input("Enter the range: "))
for i in range(n):
    j=i%2
    if j==0:
        print(i)