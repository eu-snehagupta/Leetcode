# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
# Constraints:
# 2 <= nums.length <= 10^3
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.

def two_sum(nums, target):
    if len(nums) < 2:
        return -1
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return -1


if __name__ == '__main__':
    input_list = [2,5,5]
    print(two_sum(input_list, 10))
