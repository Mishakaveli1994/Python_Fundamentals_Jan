number_of_rooms = int(input())
okay_rooms = 0
free_chairs = 0
for i in range(1, number_of_rooms + 1):
    room = input().split(' ')
    if len(room[0]) < int(room[1]):
        print(f'{abs(int(room[1]) -len(room[0]))} more chairs needed in room {i}')
    else:
        okay_rooms += 1
        free_chairs += len(room[0]) - int(room[1])
if okay_rooms == number_of_rooms:
    print(f'Game On, {free_chairs} free chairs left')