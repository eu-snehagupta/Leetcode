def remove_element(input_list, value):
    if not input_list:
        return 0
    while value in input_list:
        input_list.remove(value)
    return len(input_list)


if __name__ == '__main__':
    list1 = [0,1,2,2,3,0,4,2]
    list2 = [3,2,2,3]
    print(remove_element(list1, 2))