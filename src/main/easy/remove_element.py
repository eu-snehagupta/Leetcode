# Given an array nums and a value val, remove all instances
# of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do
# this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesnt matter what you leave beyond the new length.
#
# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means a modification
# to the input array will be known to the caller as well.
#
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 2.
# It doesnt matter what you leave beyond the returned length.
# For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.
#
# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

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