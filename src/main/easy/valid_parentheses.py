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


def is_valid_parentheses(s):
    # The stack to keep track of opening brackets.
    stack = []

    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for char in s:

        # If the character is an closing bracket
        if char in mapping:

            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack


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