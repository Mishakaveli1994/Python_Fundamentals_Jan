numbers = input().split(', ')
numbers_int_list = [int(i) for i in numbers]

for i in numbers_int_list:
    if i == 0:
        numbers_int_list.pop(numbers_int_list.index(0))
        numbers_int_list.append(0)

print(numbers_int_list)