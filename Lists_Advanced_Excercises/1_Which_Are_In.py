search_strings = input().split(', ')
words = input().split(', ')
found = []
for i in search_strings:
    for b in words:
        if i in b:
            if i not in found:
                found.append(i)
print(found)