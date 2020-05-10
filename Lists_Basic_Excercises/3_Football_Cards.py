list_of_cards = input()
split_list = list(set(list_of_cards.split(' ')))
team_a = 11
team_b = 11

for i in split_list:
    if i[0] == 'A':
        team_a -= 1
    else:
        team_b -= 1

print(f'Team A - {team_a}; Team B - {team_b}')
if team_a < 7 or team_b < 7:
    print('Game was terminated')
