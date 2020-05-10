roads = []
racers = []

while True:
    command = input()
    if command == 'END':
        break
    else:
        command_split = command.split('->')
        if command_split[0] == 'Add':
            if command_split[1] not in roads:
                roads.append(command_split[1])
                racers.append([command_split[2]])
            else:
                road_index = roads.index(command_split[1])
                racers[road_index].append(command_split[2])
        elif command_split[0] == 'Move':
            road_index = roads.index(command_split[1])
            if command_split[2] in racers[road_index]:
                racer_index = racers[road_index].index(command_split[2])
                racers[road_index].pop(racer_index)
                move_road_index = road_index = roads.index(command_split[3])
                racers[road_index].append(command_split[2])
        elif command_split[0] == 'Close':
            if command_split[1] in roads:
                road_index = roads.index(command_split[1])
                roads.pop(road_index)
                racers.pop(road_index)

# Use zip as it's a lot faster than the loop below:
# for i in range(len(roads)):
#     racer_dict[roads[i]] = racers[i]
racer_dict = dict(zip(roads, racers))
racer_number_dict = {}
for index, value in enumerate(roads):
    racer_number_dict[value] = len(racers[index])
# Sort dictionary by descending number of racers (most on top) and ascending track names
racer_number_dict = sorted(racer_number_dict.items(), key=lambda x: (-x[1], x[0]))
print('Practice sessions:')
for i in racer_number_dict:
    print(i[0])
    for b in racer_dict[i[0]]:
        print(f'++{b}')
