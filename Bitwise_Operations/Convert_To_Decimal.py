def convert_to_decimal(number, system):
# A function used to convert a number from any system to binary
# Number should be a string
    sum = 0
    position = 0
    length = len(number) - 1
    while length >=0:
        current_digit = int(number[length])
        sum += current_digit * (system ** position)
        position += 1
        length -= 1
    print(sum)

convert_to_decimal('16',8)


