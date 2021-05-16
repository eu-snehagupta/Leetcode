def plus_one(digits):
    # for i in range(len(digits)-1, -1, -1):
    #     if digits[i] + 1 == 10:
    #         digits[i] = 0
    #     else:
    #         digits[i] = digits[i] + 1
    #         break
    # return digits
    digit = ""
    for i in digits:
        digit = digit + str(i)
    return [int(d) for d in str(int(digit)+1)]


if __name__ == "__main__":
    array_of_digits = [1,2,9,9]
    array_of_digits1 = [0]
    print(plus_one(array_of_digits))