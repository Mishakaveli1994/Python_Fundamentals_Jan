def check_stats(damage_stat, health_stat, armor_stat):
    if damage_stat == 'null':
        damage_stat = 45
    else:
        damage_stat = int(damage_stat)
    if health_stat == 'null':
        health_stat = 250
    else:
        health_stat = int(health_stat)
    if armor_stat == 'null':
        armor_stat = 10
    else:
        armor_stat = int(armor_stat)
    return damage_stat, health_stat, armor_stat


dragon_dict = {}
dragon_average_stats = {}
dragon_count = int(input())
for i in range(dragon_count):
    command = input().split(' ')
    dr_type, name, damage, health, armor = command[0], command[1], command[2], command[3], command[4]
    damage, health, armor = check_stats(damage, health, armor)
    if dr_type not in dragon_dict:
        dragon_dict[dr_type] = {}
    dragon_dict[dr_type][name] = {'damage': damage, 'health': health, 'armor': armor}

for i in dragon_dict.keys():
    dragon_dict[i] = dict(sorted(dragon_dict[i].items()))

for item in dragon_dict.keys():
    for k in dragon_dict[item]:
        dragon_average_stats.setdefault(item, {'armor': 0, 'damage': 0, 'health': 0})
        dragon_average_stats[item]['health'] += dragon_dict[item][k]['health']
        dragon_average_stats[item]['armor'] += dragon_dict[item][k]['armor']
        dragon_average_stats[item]['damage'] += dragon_dict[item][k]['damage']

for i in dragon_average_stats:
    average_armor = dragon_average_stats[i]['armor'] / len(dragon_dict[i])
    average_health = dragon_average_stats[i]['health'] / len(dragon_dict[i])
    average_damage = dragon_average_stats[i]['damage'] / len(dragon_dict[i])
    print(f"{i}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for k, v in dragon_dict[i].items():
        dragon_damage = dragon_dict[i][k]['damage']
        dragon_armor = dragon_dict[i][k]['armor']
        dragon_health = dragon_dict[i][k]['health']
        print(f"-{k} -> damage: {dragon_damage}, health: {dragon_health}, armor: {dragon_armor}")
