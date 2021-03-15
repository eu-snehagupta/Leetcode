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
    if len(input_string) == 0 or len(input_string) % 2 != 0:
        return False
    is_valid = False
    parentheses_queue = []
    for element in input_string:
        if element in "({[":
            parentheses_queue.append(element)
            is_valid = False
        else:
            if len(parentheses_queue) == 0:
                return False
            if element == ")" and parentheses_queue.pop() == "(":
                is_valid = True
            elif element == "}" and parentheses_queue.pop() == "{":
                is_valid = True
            elif element == "]" and parentheses_queue.pop() == "[":
                is_valid = True
            else:
                return False
    if len(parentheses_queue) != 0:
        return False
    return is_valid


if __name__ == '__main__':
    if is_valid_parentheses("()") == True:
        print("Pass:1")
    else:
        print("Fail:1")
    if is_valid_parentheses("()[]{}") == True:
        print("Pass:2")
    else:
        print("Fail:2")
    if is_valid_parentheses("{[]}") == True:
        print("Pass:3")
    else:
        print("Fail:3")
    if is_valid_parentheses("(]") == False:
        print("Pass:4")
    else:
        print("Fail:4")
    if is_valid_parentheses("([)]") == False:
        print("Pass:5")
    else:
        print("Fail:5")
    if is_valid_parentheses("[({])}") == False:
        print("Pass:6")
    else:
        print("Fail:6")
    if is_valid_parentheses("[[[]") == False:
        print("Pass:7")
    else:
        print("Fail:7")