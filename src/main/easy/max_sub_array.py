# brute force algorithm- O(N^2)
# def max_sub_array(nums):
#     max_sum = nums[0]
#     for i in range(1, len(nums)):
#         sum = 0
#         for j in range(i, len(nums)):
#             sum = sum + nums[j]
#             if sum > max_sum:
#                 max_sum = sum
#     return max_sum

# Kadane's algorithm- O(N)
def max_sub_array(nums):
    max_sum = current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = current_sum + nums[i]
        if current_sum < nums[i]:
            current_sum = nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
        if max_sum < 0 and max_sum < nums[i]:
            max_sum = nums[i]
    return max_sum


if __name__ == "__main__":
    input_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    input_nums1 = [-1]
    input_nums2 = [5, 4, -1, 7, 8]
    input_nums3 = [-1, 1, 2, 1]
    input_nums4 = [-2, 3, 1, 3]
    input_nums5 = [-7, -2, -9, -1]
    input_nums6 = [-1, 2, -3, -1, -3]
    print(max_sub_array(input_nums6))