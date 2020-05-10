def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


dwarves = {}
dwarves_color_count = {}
while True:
    command = input()
    if command == 'Once upon a time':
        break
    else:
        command_split = command.split(' <:> ')
        color_name = f"{command_split[0]}#{command_split[1]}"
        physics = int(command_split[2])
        validate_key_existing(dwarves, color_name, physics)
        if color_name in dwarves:
            dwarves[color_name] = max(dwarves[color_name], physics)

dwarves_breakdown = []
for nc, p in dwarves.items():
    split = nc.split('#')
    name = split[0]
    hat_color = split[1]
    dwarves_breakdown.append({'name': name, 'hat_color': hat_color, 'physics': p})

for i in range(len(dwarves_breakdown)):
    dwarves_color_count.setdefault(dwarves_breakdown[i]['hat_color'], 0)
    dwarves_color_count[dwarves_breakdown[i]['hat_color']] += 1
for i in range(len(dwarves_breakdown)):
    hat_color = dwarves_breakdown[i]['hat_color']
    dwarves_breakdown[i]['color_count'] = dwarves_color_count[hat_color]

ordered_breakdown = sorted(dwarves_breakdown, key=lambda x: (x['physics'], x['color_count']), reverse=True)

for i in range(len(ordered_breakdown)):
    name = ordered_breakdown[i]['name']
    hat_color = ordered_breakdown[i]['hat_color']
    physics = ordered_breakdown[i]['physics']
    print(f"({hat_color}) {name} <-> {physics}")
