#!/usr/bin/python3
def print_last_digit(number):
    number = number - (10 * int(number / 10))
    return number
