complete_string = [i for i in input()]
numbers_list = [i for i in complete_string if i.isdigit()]
non_numbers_list = [i for i in complete_string if not i.isdigit()]
numbers_list_even = [number for index, number in enumerate(numbers_list) if index % 2 == 0]
numbers_list_odd = [number for index, number in enumerate(numbers_list) if index % 2 != 0]
result_string = ''
index_count = 0
for take, skip in zip(numbers_list_even, numbers_list_odd):
    middle = non_numbers_list[index_count:index_count + int(take)]
    result_string += ''.join(middle)
    index_count += int(take) + int(skip)

print(result_string)
