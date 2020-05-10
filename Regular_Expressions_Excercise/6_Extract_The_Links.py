import re

regex = r"((www\.)([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*)(\.[a-z]+)+)"
aux = input()
while True:
    if not aux:
        break

    result = re.findall(regex, aux)
    if len(result) != 0:
        print(result[0][0])

    if not aux:
        break
    else:
        aux = input()
