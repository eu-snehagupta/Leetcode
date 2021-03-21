# Given a sorted array nums, remove the duplicates in-place
# such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by
# modifying the input array in-place with O(1) extra memory.
#
# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means a modification
# to the input array will be known to the caller as well.
#
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesnt matter what you leave beyond the returned length.
#
# Constraints:
# 0 <= nums.length <= 3 * 10**4
# -10**4 <= nums[i] <= 10**4
# nums is sorted in ascending order.

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