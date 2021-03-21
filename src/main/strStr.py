def strStr(haystack, needle):
    if not needle:
        return 0
    if needle in haystack:
        return haystack.index(needle)
    return -1


if __name__ == '__main__':
    print(strStr("", ""))
