#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = str(number)[-1]
last_dig = int(last_dig)
if last_dig < 6:
    print(f"Last digit of {number} is {last_dig} and is less than 6 and not 0")
    print() #new line
elif last_dig > 5:
    print(f"Last digit of {number} is {last_dig} and is greater than 5")
    print()
else:
    print(f"Last digit of {number} is {last_dig} and is 0")
    print()
