heroes = {}
while True:
    command = input()
    if command == 'End':
        break
    else:
        command_split = command.split(' ')
        if command_split[0] == 'Enroll':
            if command_split[1] not in heroes:
                heroes[command_split[1]] = []
            else:
                print(f"{command_split[1]} is already enrolled.")
        elif command_split[0] == 'Learn':
            if command_split[1] in heroes:
                if command_split[2] not in heroes[command_split[1]]:
                    heroes[command_split[1]] += [command_split[2]]
                else:
                    print(f"{command_split[1]} has already learnt {command_split[2]}.")
            else:
                print(f"{command_split[1]} doesn't exist.")

        elif command_split[0] == 'Unlearn':
            if command_split[1] in heroes:
                if command_split[2] in heroes[command_split[1]]:
                    heroes[command_split[1]].pop(heroes[command_split[1]].index(command_split[2]))
                else:
                    print(f"{command_split[1]} doesn't know {command_split[2]}.")
            else:
                print(f"{command_split[1]} doesn't exist.")

heroes_sorted = dict(sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])))

print("Heroes:")
for k, v in heroes_sorted.items():
    print(f"== {k}: {', '.join(v)} ")
