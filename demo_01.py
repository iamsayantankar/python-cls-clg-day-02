# Q1. Write a program to print the Even numbers. The range must be given by the user.

n = int(input("Enter the range: "))
for i in range(n):
    j = i % 2
    if j == 0:
        print(i)

# Q2. Write a program to find the factorial of  N number by taking user input.
j = 1
n = int(input("Enter the range: "))
for i in range(1, n+1):
    j = j*i
print(j)
