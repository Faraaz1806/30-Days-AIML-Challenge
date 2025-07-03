# Problem 4: Right-Angled Triangle
# Input: rows = 4
# Output:
# *
# **
# ***
# ****
n = int(input("Enter a number: \n"))
for i in range (n):
    for j in range(i+1):
        print("*", end="")
    print()