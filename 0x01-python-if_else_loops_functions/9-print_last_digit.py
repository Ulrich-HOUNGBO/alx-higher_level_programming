#!/usr/bin/python3
def print_last_digit(number):
    l_digit = 0
    if number >= 0:
        l_digit = number % (-10)
    else:
        l_digit = 10 - (number % 10)
    print('{}'.format(l_digit), end='')
    return l_digit
