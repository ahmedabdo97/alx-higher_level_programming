#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = number - (10 * int(number / 10))
if last_number == 0:
    print("Last digit of", number, "is", last_number, "and is", last_number)
elif last_number > 0:
    print("Last digit of", number, "is", last_number, "and is greater than 5")
elif last_number < 0:
    print("Last digit of", number, "is", last_number, "and is less than 6 and not 0")

