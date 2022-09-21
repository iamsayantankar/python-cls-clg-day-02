# Q1. Write a program to print the Even numbers. The range must be given by the user.

n = int(input("Enter the range: "))
for i in range(n):
    j = i % 2
    if j == 0:
        print(i)

# Q2. Write a program to find the factorial of  N number by taking user input.
j = 1
n = int(input("Enter the range: "))
for i in range(1, n + 1):
    j *= i
print(j)

# Q3. Write a program to find the Fibonacci series. The range must be given by the user.

n = int(input("Enter the range: "))
for i in range(0, n + 1):
    if i <= 1:
        print(i)
        j = 0
        k = 1
    else:
        j, k = k, j
        k = k + j
        print(k)

# nterms = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1
