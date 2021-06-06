def add_digits(num):
    while 1:
        num = sum(map(int, str(num)))
        if num < 10:
            return num


if __name__ == "__main__":
    input_number = 38
    print(add_digits(input_number))