stores = {}
while True:
    command = input()
    if command == 'END':
        break
    else:
        command_split = command.split('->')
        if command_split[0] == 'Add':
            if command_split[1] in stores:
                stores[command_split[1]] += [x for x in command_split[2].split(',')]
            else:
                for i in command_split[2]:
                    stores[command_split[1]] = [x for x in command_split[2].split(',')]
        if command_split[0] == 'Remove':
            if command_split[1] in stores:
                del stores[command_split[1]]
print('Stores list:')
# Sort first by value and then by key in a dictionary, both descending (reverse=True)
stores_listing = sorted(stores.items(), key=lambda x: (len(x[1]), x[0]), reverse=True)
for i in stores_listing:
    print(i[0])
    for b in i[1]:
        print(f'<<{b}>>')
