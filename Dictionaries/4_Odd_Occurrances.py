words = input().split(' ')
words_dict = {}
for i in words:
    if i.lower() not in words_dict:
        words_dict[i.lower()] = 1
    else:
        words_dict[i.lower()] += 1

print(' '.join([key for (key, value) in words_dict.items() if value % 2 != 0]))
