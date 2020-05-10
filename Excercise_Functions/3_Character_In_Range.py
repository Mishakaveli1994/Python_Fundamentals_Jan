def ascii_table(str1, str2):
    start = min(ord(str1), ord(str2))
    end = max(ord(str1), ord(str2))
    print(' '.join([chr(n) for n in range(start + 1, end)]))


str1 = input()
str2 = input()

ascii_table(str1, str2)
