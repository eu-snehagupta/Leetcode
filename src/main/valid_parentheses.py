# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "(]"
# Output: false
#
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


def is_valid_parentheses(input_string):
    if len(input_string) % 2 != 0:
        return False
    if input_string[0] == ")" or input_string[0] == "}" or input_string[0] == "]":
        return False
    for element in input_string:
        open_bracket_index = input_string.index(element)
        if element == "(":
            close_bracket_index = input_string.index(")", open_bracket_index)
            open_bracket = True
        elif element == "{":
            close_bracket_index = input_string.index("}", open_bracket_index)
            open_bracket = True
        elif element == "[":
            close_bracket_index = input_string.index("]", open_bracket_index)
            open_bracket = True
        if open_bracket_index % 2 == 0 and open_bracket:
            if close_bracket_index % 2 == 0:
                return False
        elif open_bracket_index % 2 != 0 and open_bracket:
            if close_bracket_index % 2 != 0:
                return False
        else:
            return True


if __name__ == '__main__':
    print(is_valid_parentheses("()"))