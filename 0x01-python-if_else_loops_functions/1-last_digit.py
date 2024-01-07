#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = number % 10
print(number)
print(last_number)

if last_number == 0:
    print("Last digit of", number, "is", last_number, "and is", last_number)
elif last_number > 5:
    print("Last digit of", number, "is", last_number, "and is greater than 5")
elif last_number < 6:
    print("Last digit of", number, "is", last_number, "and is greater than 6 and not 0")

