ship_rows = int(input())
ship_matrix = []


for i in range(ship_rows):
    field_info = [int(x) for x in input().split(' ')]
    ship_matrix.append(field_info)

destroyed_ships = 0


attacks = input().split(' ')
for i in attacks:
    attack_split = [int(b) for b in i.split('-')]
    if ship_matrix[attack_split[0]][attack_split[1]] != 0:
        ship_matrix[attack_split[0]][attack_split[1]] -= 1
        if ship_matrix[attack_split[0]][attack_split[1]] == 0:
            destroyed_ships += 1
print(destroyed_ships)
