import math


def convertDecimalToOther(number, system, binary):
    result = ''
    while number > 0:
        result = str(number % system) + result
        number = math.floor(number / system)
    count = result.count(binary)
    print(count)


number = int(input())
dec = input()
convertDecimalToOther(number, 2, dec)
