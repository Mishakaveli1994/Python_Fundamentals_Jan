import re

numbers = input()
regex = r"(?<=\b_)[a-zA-Z]+\b"
matches = re.findall(regex, numbers)

print(",".join(matches))
