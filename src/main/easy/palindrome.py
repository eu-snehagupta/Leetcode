# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.
# Constraints:
# -2^31 <= x <= 2^31 - 1

def check_reverse(digit):
    reversed_digit = 0
    while digit > reversed_digit:
        reversed_digit = reversed_digit*10 + digit % 10
        digit = digit//10
    return reversed_digit == digit or reversed_digit//10 == digit


def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    else:
        return check_reverse(x)


if __name__ == '__main__':
    print(is_palindrome(1210))
