import re

numbers = input()
regex = r"(\+359([ |-])2\2\d{3}\2\d{4}\b)"
matches = re.findall(regex, numbers)

print(", ".join(phone for phone, sep in matches))
