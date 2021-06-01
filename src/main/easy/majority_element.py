# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majority_element(nums):
    if len(nums) == 1:
        return nums[0]
    nums_dict = {}
    maj_element = -1
    for i in range(len(nums)):
        if nums_dict.get(nums[i]):
            nums_dict[nums[i]] = nums_dict[nums[i]] + 1
            if nums_dict.get(nums[i]) > (len(nums)/2):
                maj_element = nums[i]
        else:
            nums_dict[nums[i]] = 1
    return maj_element

# def majority_element(nums):
    # nums_set = list(set(nums))
    # for num in nums_set:
    #     if nums.count(num) > len(nums)/2:
    #         return num
    # return [num for num in list(set(nums)) if nums.count(num) > len(nums)/2]
    # return max(set(nums),key = nums.count)


if __name__ == "__main__":
    input_array0 = [3, 2, 3]
    input_array1 = [2, 2, 1, 1, 1, 2, 2]
    input_array2 = [1]
    print(majority_element(input_array2))