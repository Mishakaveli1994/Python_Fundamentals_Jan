from itertools import groupby

tickets = input().split(', ')
winning_symbols = ['@', '#', '$', '^']
for i in range(len(tickets)):
    tickets[i] = tickets[i].strip()

for i in tickets:
    if len(i) != 20:
        print("invalid ticket")
    else:
        group1 = groupby(i[0:10])
        group2 = groupby(i[10:])
        left = [[label, sum(1 for _ in group)] for label, group in group1 if label in winning_symbols]
        left = [[k, v] for k, v in left if v > 5]
        right = [[label, sum(1 for _ in group)] for label, group in group2 if label in winning_symbols]
        right = [[k, v] for k, v in right if v > 5]
        if len(left) and len(right) != 0:
            if left[0][0] == right[0][0]:
                symbol = left[0][0]
                total = min(left[0][1],right[0][1])
                if total == 10:
                    print(f'ticket "{i}" - {total}{symbol} Jackpot!')
                else:
                    print(f'ticket "{i}" - {total}{symbol}')
            else:
                print(f'ticket "{i}" - no match')
        else:
            print(f'ticket "{i}" - no match')
