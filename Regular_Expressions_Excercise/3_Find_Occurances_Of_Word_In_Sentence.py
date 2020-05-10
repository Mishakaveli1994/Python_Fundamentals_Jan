import re

text = input().lower()
word = input().lower()
regex = r"\b%s\b" % word
matches = re.findall(regex,text)
print(len(matches))