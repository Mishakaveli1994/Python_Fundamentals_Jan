animals = []
daily_food_limit = []
area = []

while True:
    command = input()
    if command == 'Last Info':
        break
    else:
        command_split = command.split(':')
        if command_split[0] == 'Add':
            if command_split[1] in animals:
                daily_food_limit[animals.index(command_split[1])] += int(command_split[2])
            else:
                animals.append(command_split[1])
                daily_food_limit.append(int(command_split[2]))
                area.append(command_split[3])
        elif command_split[0] == 'Feed':
            if command_split[1] in animals:
                position = animals.index(command_split[1])
                daily_food_limit[position] -= int(command_split[2])
                if daily_food_limit[position] <= 0:
                    animals.pop(position)
                    daily_food_limit.pop(position)
                    area.pop(position)
                    print(f'{command_split[1]} was successfully fed')

print('Animals:')
food_need_sorted = {}
for index,value in enumerate(daily_food_limit):
    if value in food_need_sorted:
        food_need_sorted[value] += [animals[index]]
    else:
        food_need_sorted[value] = [animals[index]]

if len(food_need_sorted) != 0:
    for index in sorted(food_need_sorted.keys(),reverse=True):
        for i in sorted(food_need_sorted[index]):
            print(f'{i} -> {index}g')

still_hungry_area = {}
for value in area:
    if value in still_hungry_area:
        still_hungry_area[value] += 1
    else:
        still_hungry_area[value] = 1
still_hungry_area = sorted(still_hungry_area.items(), key=lambda x: x[1],reverse=True)
print('Areas with hungry animals:')
if len(still_hungry_area) != 0:
    for value in still_hungry_area:
        print(f'{value[0]} : {value[1]}')