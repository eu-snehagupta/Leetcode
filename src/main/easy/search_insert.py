# Given a sorted array of distinct integers and
# a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Constraints:
# 1 <= nums.length <= 10**4
# -10**4 <= nums[i] <= 10**4
# nums contains distinct values sorted in ascending order.
# -10**4 <= target <= 10**4

def search_insert(nums, target):
    nums.append(target)
    nums.sort()
    return nums.index(target)


if __name__ == '__main__':
    input_array = [1]
    print(search_insert(input_array, 0))