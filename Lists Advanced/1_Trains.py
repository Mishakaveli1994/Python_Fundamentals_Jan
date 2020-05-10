wagons = [int(i) for i in ['0'] * int(input())]

while True:
    command = input()
    if command == 'End':
        break
    else:
        command_split = command.split(' ')
        if command_split[0] == 'add':
            wagons[len(wagons)-1] += int(command_split[1])
        elif command_split[0] == 'insert':
            wagons[int(command_split[1])] += int(command_split[2])
        elif command_split[0] == 'leave':
            wagons[int(command_split[1])] -= int(command_split[2])
print(wagons)