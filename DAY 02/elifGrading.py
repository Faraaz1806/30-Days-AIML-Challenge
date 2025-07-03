# Problem 1: Age Category
# Tum ek input loge (user ki age) aur output dena hoga:
# Below 18 → "Teenager"
# 18 to 59 → "Adult"
# 60+ → "Senior Citizen"
age = int(input("Enter your Age: \n"))
if age <= 18:
    print("User is a Teenager")
elif age > 18 and age <= 59:
    print("User is an Adult")
elif age >= 60:
    print("User is a Senior Citizen")
else:
    print("Invalid Input")