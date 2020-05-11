skill = [i for i in input()]

while True:
    command = input()
    if command == 'For Azeroth':
        break
    else:
        command_split = command.split(' ')
        if command_split[0] == 'GladiatorStance':
            skill = [i.upper() for i in skill]
            print(''.join([i for i in skill]))
        elif command_split[0] == 'DefensiveStance':
            skill = [i.lower() for i in skill]
            print(''.join([i for i in skill]))
        elif command_split[0] == 'Dispel':
            if int(command_split[1]) < len(skill):
                skill[int(command_split[1])] = command_split[2]
                print("Success!")
            else:
                print("Dispel too weak.")
        elif command_split[0] == 'Target':
            if command_split[1] == 'Change':
                string = ''.join(skill)
                string = string.replace(command_split[2], command_split[3])
                print(string)
                skill = [i for i in string]
            elif command_split[1] == 'Remove':
                string = ''.join(skill)
                string = string.replace(command_split[2], '')
                print(string)
                skill = [i for i in string]
            else:
                print("Command doesn't exist!")
        else:
            print("Command doesn't exist!")
