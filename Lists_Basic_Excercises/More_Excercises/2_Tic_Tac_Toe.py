line1 = input().split(' ')
line2 = input().split(' ')
line3 = input().split(' ')
won_players = []

if line1[0] == line2[0] == line3[0]:
    if line1[0] != 0:
        won_players.append(line1[0])

if line1[0] == line2[1] == line3[2]:
    if line1[0] != 0:
        won_players.append(line1[0])

if line1[0] == line1[1] == line1[2]:
    if line1[0] != 0:
        won_players.append(line1[0])

if line3[2] == line2[2] == line1[2]:
    if line3[2] != 0:
        won_players.append(line3[2])

if line3[2] == line3[1] == line3[0]:
    if line3[2] != 0:
        won_players.append(line3[2])

if line1[2] == line2[1] == line3[0]:
    if line1[2] != 0:
        won_players.append(line1[2])

if line1[1] == line2[1] == line3[1]:
    if line1[1] != 0:
        won_players.append(line1[1])

if line2[2] == line2[1] == line2[0]:
    if line2[2] != 0:
        won_players.append(line2[2])

if won_players[0] == '1':
    print('First player won')
elif won_players[0] == '2':
    print('Second player won')
else:
    print('Draw!')
