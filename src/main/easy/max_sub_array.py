def max_sub_array(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum = sum + nums[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum


if __name__ == "__main__":
    input_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    input_nums1 = [-1]
    input_nums2 = [5, 4, -1, 7, 8]
    print(max_sub_array(input_nums1))