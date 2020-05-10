number = input()
number_sep = number.split(' ')

for i in range(len(number_sep)):
    if int(number_sep[i]) < 0:
        number_sep[i] = abs(int(number_sep[i]))
    elif int(number_sep[i]) > 0:
        number_sep[i] = int(number_sep[i]) * -1
    elif int(number_sep[i]) == 0:
        number_sep[i] = 0
print(number_sep)
