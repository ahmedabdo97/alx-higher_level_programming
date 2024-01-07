#!/usr/bin/python3
for letter in range(97, 123):
    q = chr(113)
    e = chr(101)
    letter_alp = chr(letter)
    if letter_alp == q or letter_alp == e:
        continue
    else:
        print("{}".format(letter_alp), end="")
