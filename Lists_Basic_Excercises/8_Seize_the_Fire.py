fire_level = input().split('#')
filtered_fire_level = []
available_water = int(input())
effort = 0
total_fire = 0

for i in fire_level:
    fire_filtered = i.split(' ')
    if fire_filtered[0] == 'Low' and 1 <= int(fire_filtered[2]) <= 50:
        filtered_fire_level.append(i)
    elif fire_filtered[0] == 'Medium' and 51 <= int(fire_filtered[2]) <= 80:
        filtered_fire_level.append(i)
    elif fire_filtered[0] == 'High' and 81 <= int(fire_filtered[2]) <= 125:
        filtered_fire_level.append(i)

if len(filtered_fire_level) >= 0:
    print('Cells:')

for i in filtered_fire_level:
    fire_filtered = i.split(' ')
    if int(fire_filtered[2]) <= available_water:
        print(f' - {fire_filtered[2]}')
        available_water -= int(fire_filtered[2])
        effort += int(fire_filtered[2]) * 0.25
        total_fire += int(fire_filtered[2])

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')