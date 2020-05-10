integer_list = [int(i) for i in input().split(' ')]


def exchange(list):
    global integer_list
    index = int(command_list[1])
    if index < len(integer_list):
        integer_list = (integer_list[index + 1:] + integer_list[:index + 1:])
    else:
        print('Invalid index')


def max_num(list):
    type_int = list[1]
    if type_int == 'even':
        try:
            valid_numbers = [x for x in integer_list if x % 2 == 0]
            indices = max([i for i, x in enumerate(integer_list) if x == max(valid_numbers)])
            print(indices)

        except:
            print('No matches')
    elif type_int == 'odd':
        try:
            valid_numbers = [x for x in integer_list if x % 2 != 0]
            indices = max([i for i, x in enumerate(integer_list) if x == max(valid_numbers)])
            print(indices)

        except:
            print('No matches')


def min_num(list):
    type_int = list[1]
    if type_int == 'even':
        try:
            valid_numbers = [x for x in integer_list if x % 2 == 0]
            indices = max([i for i, x in enumerate(integer_list) if x == min(valid_numbers)])
            print(indices)
        except:
            print('No matches')
    elif type_int == 'odd':
        try:
            valid_numbers = [x for x in integer_list if x % 2 != 0]
            indices = max([i for i, x in enumerate(integer_list) if x == min(valid_numbers)])
            print(indices)
        except:
            print('No matches')


def first_count(list):
    number_count = list[1]
    first_count_number = []
    if int(number_count) > len(integer_list):
        print('Invalid count')
    else:
        if list[2] == 'even':
            first_count_number = ([int(i) for i in integer_list if int(i) % 2 == 0])
        elif list[2] == 'odd':
            first_count_number = ([int(i) for i in integer_list if int(i) % 2 != 0])

        if len(first_count_number) > int(number_count):
            first_count_number = first_count_number[:int(number_count)]

        print(first_count_number)


def last_count(list):
    number_count = list[1]
    last_count_number = []
    if int(number_count) > len(integer_list):
        print('Invalid count')
    else:
        if list[2] == 'even':
            last_count_number = ([int(i) for i in integer_list if int(i) % 2 == 0])
        elif list[2] == 'odd':
            last_count_number = ([int(i) for i in integer_list if int(i) % 2 != 0])

        if len(last_count_number) > int(number_count):
            last_count_number = last_count_number[len(last_count_number) - int(number_count):]

        print(last_count_number)


while True:
    command = input()
    command_list = command.split(' ')

    if command_list[0] == 'end':
        print(integer_list)
        break

    elif command_list[0] == 'exchange':
        exchange(command_list)

    elif command_list[0] == 'max':
        max_num(command_list)

    elif command_list[0] == 'min':
        min_num(command_list)

    elif command_list[0] == 'first':
        first_count(command_list)

    elif command_list[0] == 'last':
        last_count(command_list)
