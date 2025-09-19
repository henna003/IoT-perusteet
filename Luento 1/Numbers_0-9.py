import time
time.sleep(0.1) # Wait for USB to become ready

print("Ready to go!")
number = 0
while number < 10:
    print(f"Loop number: {number}")
    number += 1
print("Loop finished")