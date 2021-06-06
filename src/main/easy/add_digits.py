def add_digits(num):
    if num < 10:
        return num
    else:
        return add_digits(sum(map(int, str(num))))


if __name__ == "__main__":
    input_number = 38
    print(add_digits(input_number))