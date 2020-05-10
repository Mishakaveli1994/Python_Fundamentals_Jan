import re

numbers = input()
regex = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(regex, numbers)

for i in matches:
    print(i.group(0), end=' ')