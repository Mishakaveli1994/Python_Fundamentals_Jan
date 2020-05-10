digit_list = input().split(' ')
message_string = [i for i in input()]
message = ''
for i in digit_list:
    sum_of_digits = sum([int(b) for b in i])
    if sum_of_digits > len(message_string):
        message += message_string[sum_of_digits % len(message_string)]
        message_string.pop(sum_of_digits % len(message_string))
    else:
        message += message_string[sum_of_digits]
        message_string.pop(sum_of_digits)
print(message)