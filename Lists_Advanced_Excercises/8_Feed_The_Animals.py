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
for i in range(len(animals)):
    print(f'{animals[i]} -> {daily_food_limit[i]}g')
print('Areas with hungry animals:')
area_dict = {}
for index, name in enumerate(area):
    if name not in area_dict:
        area_dict.update({name: 1})
    else:
        area_dict[name] += 1
# you can take the input as integers also this'
# will work for that also for eg:{1:2,3:4,4:3,2:1,0:0}
# y = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}

l = list(area_dict.items())  # convet the given dict. into list
# In Python Dictionary, items() method is used to return the list
# with all dictionary keys with values.
l.sort()  # sort the list
# print('Ascending order is', l)  # this print the sorted list

l = list(area_dict.items())
l.sort(reverse=True)  # sort in reverse order
# print('Descending order is', l)

dict = dict(l)  # convert the list in dictionary

# print("Dictionary", dict)  # the desired output is this sorted dictionary
# sorted_list = {k: v for k, v in sorted(area_dict.items(), key=lambda x: x[1])}
# sort dictionary

for i, b in dict.items():
    print(f'{i} : {b}')
