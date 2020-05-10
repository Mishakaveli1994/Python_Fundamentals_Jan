time = input().split(' ')
middle = len(time) // 2
racer_time1 = time[:middle]
racer_time2 = time[middle + 1:]
racer_time2.reverse()
racer_times = [racer_time1, racer_time2]
racer1 = 0
racer2 = 0

for index, value in enumerate(racer_times):
    if index == 0:
        for b in value:
            if int(b) != 0:
                racer1 += int(b)
            else:
                racer1 *= 0.8
    elif index == 1:
        for b in value:
            if int(b) != 0:
                racer2 += int(b)
            else:
                racer2 *= 0.8
if racer1 < racer2:
    print(f'The winner is left with total time: {racer1:.1f}')
else:
    print(f'The winner is right with total time: {racer2:.1f}')