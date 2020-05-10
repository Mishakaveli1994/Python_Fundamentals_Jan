import math
def convertDecimalToOther(number,system):
    result = ''
    while number > 0:
        result = str(number % system) + result
        number = math.floor(number / system)
    print(result)

convertDecimalToOther(14,8)