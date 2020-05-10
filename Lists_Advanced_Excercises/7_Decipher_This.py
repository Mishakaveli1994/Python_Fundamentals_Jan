cypher = input().split(' ')
final_sentance = []
for index, word in enumerate(cypher):
    word_split = word.split()
    numbers = list(filter(lambda i: i.isdigit(), word_split[0]))
    ascii = chr(int(''.join(numbers)))
    word_split = word_split[0][len(numbers):]
    word_split = list(ascii + word_split)
    word_split[1], word_split[len(word_split) - 1] = word_split[len(word_split) - 1], word_split[1]
    word_string = ''.join(word_split)
    final_sentance.append(word_string)
print(' '.join(final_sentance))
