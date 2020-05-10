gifts = input().split(' ')

while True:
    item = input()
    if item == 'No Money':
        break
    else:
        list_item = item.split(' ')
        if list_item[0] == 'OutOfStock':
            for i in gifts:
                if i == list_item[1]:
                    gifts[gifts.index(list_item[1])] = 'None'
        elif list_item[0] == 'Required':
            if 0 <= int(list_item[2]) <= len(gifts) - 1:
                gifts[int(list_item[2])] = list_item[1]
        elif list_item[0] == 'JustInCase':
            gifts[len(gifts) - 1] = list_item[1]

gifts = list(filter(lambda a: a != 'None', gifts))

print(' '.join(gifts))
