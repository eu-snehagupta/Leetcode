# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.


# lets first check if s a palindrome
def palindrome(s):
    mid = len(s) // 2
    if len(s) % 2 != 0:
        if s[:mid] == s[:mid:-1]:
            return s
    else:
        if s[:mid] == s[:mid - 1:-1]:
            return s
    return ""


def longest_palindrome(s):
    if palindrome(s) == s:
        return s
    longest = s[0]
    for i in range(0, len(s)):
        for j in range(1, len(s)+1):
            current = palindrome(s[i:j])
            if len(current) > len(longest):
                longest = current
    return longest


if __name__ == "__main__":
    input_string0 = "babad"
    input_string1 = "cbbd"
    input_string2 = "a"
    input_string3 = "ac"
    input_string4 = "bb"
    print(longest_palindrome(input_string4))