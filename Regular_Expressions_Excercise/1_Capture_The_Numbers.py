import re

expression = r"(\d+)"
aux = input()
while True:
    if not aux:
        break

    result = re.findall(expression, aux)
    for num in result:
        print(num, end=" ")

    if not aux:
        break
    aux = input()
