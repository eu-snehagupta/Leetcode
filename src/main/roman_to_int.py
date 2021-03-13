# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two ones added together.
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest
# from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
#
# There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given a roman numeral, convert it to an integer.
#
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


# def roman_to_int(input_string):
#     roman_string = ["I", "V", "X", "L", "C", "D", "M"]
#     roman_string_value = [1, 5, 10, 50, 100, 500, 1000]
#     converted_value = 0
#     index_previous = len(roman_string_value)
#     for element in input_string:
#         index_current = roman_string.index(element)
#         if index_previous >= index_current:
#             converted_value = converted_value + roman_string_value[index_current]
#         else:
#             converted_value += (roman_string_value[index_current] - 2 * (roman_string_value[index_previous]))
#         index_previous = index_current
#     return converted_value

def roman_to_int(input_string):
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    converted_value = 0
    previous_value = 0
    for i in range(len(input_string)):
        current_value = roman_map[input_string[i]]
        if current_value > previous_value:
            converted_value += current_value - 2*previous_value
        else:
            converted_value += current_value
        previous_value = current_value
    return converted_value


if __name__ == '__main__':
    print(roman_to_int("MCMXCIV"))
