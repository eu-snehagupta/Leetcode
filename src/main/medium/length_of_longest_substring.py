# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def length_of_longest_substring(s):
    len_longest_substring = 0
    unique_list = []
    for element in s:
        if element in unique_list:
            if unique_list[-1] == element:
                unique_list.clear()
            else:
                repeated_index = unique_list.index(element)
                unique_list = unique_list[repeated_index+1:]
        unique_list.append(element)
        if len(unique_list) > len_longest_substring:
            len_longest_substring = len(unique_list)
    return len_longest_substring


if __name__ == "__main__":
    input_string0 = "abcabcbb"
    input_string1 = "pwwkew"
    input_string2 = "bbbbb"
    input_string3 = ""
    input_string4 = "aab"
    input_string5 = "dvdf"
    print(length_of_longest_substring(input_string5))