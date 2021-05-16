def length_of_last_word(string):
    # if string.isspace() is True or string == "":
    #     return 0
    # words = string.split(" ")
    # for i in range(len(words)-1, -1, -1):
    #     if not (words[i] == ""):
    #         return len(words[i])
    return len(string.strip().split(" ")[-1])


if __name__ == "__main__":
    input_string = "Today is a nice day"
    input_string1 = "   "
    input_string2 = "a "
    input_string3 = ""
    print(length_of_last_word(input_string2))