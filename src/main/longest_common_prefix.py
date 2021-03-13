# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Constraints:
# 0 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

def shortest_word(string_array):
    length = len(string_array[0])
    for element in string_array:
        if length > len(element):
            length = len(element)
    return length


def longest_common_prefix(string_array):
    if len(string_array) == 0:
        return ""
    if len(string_array) == 1:
        return string_array[0]
    first_word = string_array[0]
    common_prefix = ""
    current_index = 0
    max_index = shortest_word(string_array)
    common = True

    while common and current_index in range(max_index):
        for i in range(1, len(string_array)):
            if first_word[current_index] != string_array[i][current_index]:
                common = False
                return common_prefix
        common_prefix += first_word[current_index]
        current_index += 1
    return common_prefix


if __name__ == '__main__':
    strings = ["dog", "d", "dust"]
    print(longest_common_prefix(strings))
