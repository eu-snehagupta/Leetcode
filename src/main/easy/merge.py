def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1.pop()
    for i in range(n):
        nums1.append(nums2[i])
    nums1.sort()
    print(nums1)


if __name__ == "__main__":
    array1 = [1,2,3,0,0,0]
    array2 = [2,5,6]
    merge(array1, 3, array2, 3)
    # array1 = [1]
    # array2 = []
    # merge(array1, 1, array2, 0)
