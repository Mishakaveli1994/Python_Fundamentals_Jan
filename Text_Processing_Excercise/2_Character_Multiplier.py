from itertools import zip_longest

text = input().split(' ')
part1 = text[0]
part2 = text[1]
sum = 0
for l1, l2 in zip_longest(part1, part2, fillvalue=' '):
    if l1 == ' ':
        sum += ord(str(l2))
    elif l2 == ' ':
        sum += ord(str(l1))
    else:
        sum += ord(str(l1)) * ord(str(l2))
print(sum)
