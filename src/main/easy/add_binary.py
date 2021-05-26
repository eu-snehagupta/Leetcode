# Given two binary strings a and b, return their sum as a binary string.
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"


def add_binary(digit_a,digit_b):
    list_a = list(int(a) for a in digit_a)
    list_b = list(int(b) for b in digit_b)
    result = []
    carry = 0
    while list_a or list_b:
        temp = 0
        temp_a = 0
        temp_b = 0
        if list_a:
            temp_a = list_a.pop()
        if list_b:
            temp_b = list_b.pop()
        temp = temp_a + temp_b + carry
        if temp == 2:
            result.append(0)
            carry = 1
        elif temp == 3:
            result.append(1)
            carry = 1
        else:
            result.append(temp)
            carry = 0
    if carry == 1:
        result.append(carry)
    return "".join(str(i) for i in list(reversed(result)))


if __name__ == '__main__':
    a = "10"
    b = "100"
    print(add_binary(a,b))

