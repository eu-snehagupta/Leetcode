# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Constraints:
# -2^31 <= x <= 2^31 - 1

def reverse(digit):
    reversed_digit = 0
    while digit > 0:
        reversed_digit = reversed_digit*10 + digit % 10
        digit = digit//10  # use //
    if not(-2**31 <= reversed_digit <= 2**31 - 1):
        return 0
    else:
        return reversed_digit


def reverse_integer(x):
    if not (-2**31 <= x <= 2**31 - 1):   # use **
        return 0
    if x < 0:
        return -reverse(-x)
    else:
        return reverse(x)


if __name__ == '__main__':
    print(reverse_integer(123))
