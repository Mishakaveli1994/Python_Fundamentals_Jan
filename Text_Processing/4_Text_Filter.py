banned_words = input().split(', ')
text = input()
for i in banned_words:
    text = text.replace(i, len(i) * '*')

print(text)
