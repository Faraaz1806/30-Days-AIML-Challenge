#lists are used to store multiple things...
fruits = ["apple","banana","mango"]
#here fruit becomes a single thing present in the list in this case it can be apple, banana, mango
for fruit in fruits:
    print(fruit)

for fruit in fruits:
    if fruit == "mango":
        print("Yes mango is there in list")
    else:
        print("No")
        
def greet(name):
    print("Hello", name)
name = input("Enter ur Name..")
greet(name)