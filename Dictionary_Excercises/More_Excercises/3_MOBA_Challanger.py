def validate_key_existing(dictionary, key):
    if key not in dictionary:
        dictionary[key] = {}


total_skill = {}
players = {}
while True:
    command = input()
    if command == 'Season end':
        break
    else:
        if ' -> ' in command:
            command_split = command.split(' -> ')
            player, position, skill = command_split[0], command_split[1], int(command_split[2])
            validate_key_existing(players, player)
            total_skill.setdefault(player, 0)
            total_skill[player] += skill
            if position not in players[player]:
                players[player][position] = skill
            else:
                if players[player][position] < skill:
                    total_skill[player] -= players[player][position]
                    players[player][position] = skill
                elif players[player][position] > skill:
                    total_skill[player] -= skill
                elif players[player][position] == skill:
                    total_skill[player] -= players[player][position]

        else:
            command_split = command.split(' vs ')
            player1, player2 = command_split[0], command_split[1]
            if player1 in players and player2 in players:
                common_position = len(set(players[player1]).intersection(players[player2]))
                if common_position > 0:
                    if total_skill[player1] > total_skill[player2]:
                        del total_skill[player2]
                        del players[player2]
                    elif total_skill[player1] < total_skill[player2]:
                        del total_skill[player1]
                        del players[player1]

total_skill_sorted = dict(sorted(total_skill.items(), key=lambda x: (-x[1], x[0])))
for p, v in players.items():
    players[p] = dict(sorted(players[p].items(), key=lambda x: (-x[1], x[0])))

for p, v in total_skill_sorted.items():
    print(f"{p}: {v} skill")
    for c, k in players[p].items():
        print(f"- {c} <::> {k}")
