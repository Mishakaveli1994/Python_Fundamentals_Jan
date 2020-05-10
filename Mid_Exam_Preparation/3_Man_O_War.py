pirate_ship_status = [int(x) for x in input().split('>')]
warship_status = [int(x) for x in input().split('>')]
max_possible_health = int(input())
while True:
    command = input()
    if command == 'Retire':
        print(f"Pirate ship status: {sum([i for i in pirate_ship_status])}")
        print(f"Warship status: {sum([i for i in warship_status])}")
        break
    else:
        command_split = command.split(' ')
        if command_split[0] == 'Fire':
            index, damage = int(command_split[1]), int(command_split[2])
            if 0 <= index < len(warship_status):
                if warship_status[index] - damage <= 0:
                    print('You won! The enemy ship has sunken.')
                    break
                else:
                    warship_status[index] -= damage
        if command_split[0] == 'Defend':
            start_index, end_index, damage = int(command_split[1]), int(command_split[2]), int(command_split[3])
            if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
                if len([i for i in pirate_ship_status[start_index:end_index] if i - damage <= 0]) > 0:
                    print("You lost! The pirate ship has sunken.")
                    break
                else:
                    for i, h in enumerate(pirate_ship_status[start_index:end_index + 1], start_index):
                        pirate_ship_status[i] -= damage
        if command_split[0] == 'Repair':
            index, health = int(command_split[1]), int(command_split[2])
            if 0 <= index < len(pirate_ship_status):
                if pirate_ship_status[index] + health > max_possible_health:
                    pirate_ship_status[index] = max_possible_health
                else:
                    pirate_ship_status[index] += health
        if command_split[0] == 'Status':
            need_repairs = [b for b in pirate_ship_status if b < max_possible_health * 0.2]
            print(f"{len(need_repairs)} sections need repair.")
