# # Q1. Write a program to print the Even numbers. The range must be given by the user.
#
# n = int(input("Enter the range: "))
# for i in range(n):
#     j = i % 2
#     if j == 0:
#         print(i)
#
# # Q2. Write a program to find the factorial of  N number by taking user input.
# j = 1
# n = int(input("Enter the range: "))
# for i in range(1, n + 1):
#     j *= i
# print(j)
#
# # Q3. Write a program to find the Fibonacci series. The range must be given by the user.
#
# n = int(input("Enter the range: "))
# for i in range(0, n + 1):
#     if i <= 1:
#         print(i)
#         j = 0
#         k = 1
#     else:
#         j, k = k, j
#         k = k + j
#         print(k)

# Q5. Write a Python program to get the largest number from a list.
n = int(input("Enter the range: "))
a = []
for i in range(0, n):
    b = int(input("Enter the number: "))
    a.append(b)
a.sort()
c = len(a)
print("(Type 01) The largest number is: ", a[c-1])

print("(Type 02) The largest number is: ", max(a))
