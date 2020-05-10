import re

text = input()
regex = r"(\b(?<!(\.|-|_))[a-zA-Z0-9]+[-_.]?[a-zA-Z0-9]+@(?![\.|-|_])[a-zA-Z0-9-_.]+\.[a-z]+\b)"
matches = re.findall(regex, text)


for i in matches:
    print(i[0])