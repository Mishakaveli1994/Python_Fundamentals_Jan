synonym_list = {}
number_of_words = int(input())
for i in range(number_of_words):
    word = input()
    synonym = input()
    if word not in synonym_list:
        synonym_list[word] = [synonym]
    else:
        synonym_list[word] += [synonym]

for word in synonym_list:
    print(f"{word} - {', '.join(synonym_list[word])}")