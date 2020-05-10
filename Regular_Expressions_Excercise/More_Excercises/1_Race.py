import re

regex_names = r'([a-zA-Z])'
regex_digits = r'([0-9])'
racers = {}
racers_input = input().split(', ')
for i in racers_input:
    racers[i] = 0

while True:
    command = input()
    if command == 'end of race':
        break
    else:
        name = ''.join(re.findall(regex_names, command))
        time = sum(int(i) for i in re.findall(regex_digits, command))
        if name in racers:
            racers[name] += time
racers_ordered = sorted(racers.items(), key=lambda x: -x[1])

for i,b in enumerate(racers_ordered,1):
    if i == 1:
        print(f"1st place: {b[0]}")
    elif i == 2:
        print(f"2nd place: {b[0]}")
    elif i == 3:
        print(f"3rd place: {b[0]}")