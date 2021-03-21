def remove_duplicates(input_list):
    if len(input_list) <= 1:
        return len(input_list)
    prev = input_list[0]
    repeat = "*"
    for i in range(1, len(input_list)):
        if input_list[i] == prev:
            input_list[i] = repeat
        else:
            prev = input_list[i]
    while repeat in input_list:
        input_list.remove(repeat)
    return len(input_list)

# if sys.maxsize in input_list:
    #     input_list.sort()
    #     index = input_list.index(sys.maxsize)
    #     for i in reversed(range(index, len(input_list))):
    #         input_list.remove(input_list[i])


if __name__ == '__main__':
    list1 = [0,0,1,1,1,2,2,3,3,4]
    list2 = [1]
    print(remove_duplicates(list1))