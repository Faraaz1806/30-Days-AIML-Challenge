# Problem 3: Countdown Timer
# User se ek number lo (e.g. 5)
# Print karo countdown jaise:
# makefile
# Copy
# Edit
# Countdown: 5  
# Countdown: 4  
# ...  
# Countdown: 1  
# Liftoff!
count = int(input("Enter a number to start countdown: \n"))
while (True):
    print("Countdown ",count)
    count = count - 1
    if(count == 0):
        print("Liftoff")
        break