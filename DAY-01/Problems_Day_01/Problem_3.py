#Ask the user for a number. Check whether it is a prime number (only divisible by 1 and itself).
num = int(input("Enter the no to check whether its prime or not: \n"))
b = 0
for i in range (2,num):
    if num%i == 0:
        b = 1
        break
if b == 0 :
    print("Number ",num," is Prime")
else:
    print("Number ",num," is not Prime")