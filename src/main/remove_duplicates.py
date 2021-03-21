import sys


def remove_duplicates(input_list):
    if len(input_list) < 1:
        return
    prev = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] == prev:
            input_list[i] = sys.maxsize
        else:
            prev = input_list[i]
    if sys.maxsize in input_list:
        input_list.sort()
        index = input_list.index(sys.maxsize)
        for i in reversed(range(index, len(input_list))):
            input_list.remove(input_list[i])
    return len(input_list)


if __name__ == '__main__':
    list1 = [0,0,1,1,1,2,2,3,3,4]
    list2 = [1]
    print(remove_duplicates(list2))