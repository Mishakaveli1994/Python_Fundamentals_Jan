def validate_key_existing(dictionary, key):
    if key not in dictionary:
        dictionary[key] = 0


def print_dictionary(dictionary, separator):
    for k, v in dictionary.items():
        print(separator.format(k, v))


contest_points = {}
participants = {}
while True:
    command = input()
    if command == "no more time":
        break
    else:
        command_split = command.split(' -> ')
        user, contest, points = command_split[0], command_split[1], int(command_split[2])
        if contest not in participants:
            participants[contest] = {}
        validate_key_existing(participants[contest], user)
        participants[contest][user] = max(participants[contest][user], points)

for i in participants:
    participants[i] = dict(sorted(participants[i].items(), key=lambda x: (-x[1], x[0])))
for i in participants:
    for b, v in participants[i].items():
        if b not in contest_points:
            contest_points[b] = v
        else:
            contest_points[b] += v

contest_points = dict(sorted(contest_points.items(), key=lambda x: (-x[1], x[0])))

for i in participants:
    print(f"{i}: {len(participants[i])} participants")
    for n, b in enumerate(participants[i].items(), 1):
        print(f"{n}. {b[0]} <::> {b[1]}")
print(f"Individual standings:")
for i, b in enumerate(contest_points.items(), 1):
    print(f"{i}. {b[0]} -> {b[1]}")
