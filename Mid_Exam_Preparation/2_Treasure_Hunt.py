treasure_chest_content = input().split('|')

while True:
    command = input()
    if command == 'Yohoho!':
        break
    else:
        command_split = command.split(' ', maxsplit=1)
        if command_split[0] == 'Loot':
            for i in command_split[1].split(' '):
                if i not in treasure_chest_content:
                    treasure_chest_content.insert(0, i)
        elif command_split[0] == 'Drop':
            if int(command_split[1]) <= len(treasure_chest_content):
                removed_item = treasure_chest_content.pop(int(command_split[1]))
                treasure_chest_content.append(removed_item)
        elif command_split[0] == 'Steal':
            if int(command_split[1]) <= len(treasure_chest_content):
                print(f"{', '.join(treasure_chest_content[len(treasure_chest_content) - int(command_split[1]):])}")
                treasure_chest_content = treasure_chest_content[0:len(treasure_chest_content) - int(command_split[1])]
            else:
                print(f"{', '.join(treasure_chest_content)}")
                treasure_chest_content = []
item_len = 0
for i in treasure_chest_content:
    item_len += len(i)

if len(treasure_chest_content) > 0:
    print(f"Average treasure gain: {item_len/len(treasure_chest_content):.2f} pirate credits.")
else:
    print(f'Failed treasure hunt.')