events = input().split('|')
energy = 100
coins = 100
day_complete = 0

for i in events:
    event_split = i.split('-')
    split1 = event_split[0]
    split2 = event_split[1]
    if split1 == 'rest':
        if energy + int(split2) > 100:
            print(f'You gained {100 - energy} energy.')
            energy = 100
        else:
            print(f'You gained {split2} energy.')
            energy += int(split2)
        print(f'Current energy: {energy}.')
    elif split1 == 'order':
        if energy >= 30:
            coins += int(split2)
            energy -= 30
            print(f'You earned {split2} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins - int(split2) > 0:
            print(f'You bought {split1}.')
            coins -= int(split2)
        else:
            print(f'Closed! Cannot afford {split1}.')
            day_complete = 1
            break

if day_complete == 0:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
