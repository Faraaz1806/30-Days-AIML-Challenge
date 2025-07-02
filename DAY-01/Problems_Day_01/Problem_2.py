#Q 2 : Sum of Numbers from 1 to N
#Input a number n, calculate the sum from 1 to n using a loop.
num = int(input("Enter a number: \n"))
n = 0
for i in range(num+1):
    n = n + i
print(n)