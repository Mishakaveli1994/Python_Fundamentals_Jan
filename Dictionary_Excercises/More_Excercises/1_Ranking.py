def print_dictionary(dictionary, separator):
    for k, v in dictionary.items():
        print(separator.format(k, v))


contests = {}
participants = {}

while True:
    command = input()
    if command == 'end of contests':
        break
    else:
        command_split = command.split(':')
        contest = command_split[0]
        password = command_split[1]
        contests[contest] = password

while True:
    command = input()
    if command == 'end of submissions':
        break
    else:
        command_split = command.split('=>')
        contest, password, username, points = command_split[0], command_split[1], command_split[2], int(
            command_split[3])
        if contest in contests and password == contests[contest]:
            if username not in participants:
                participants[username] = {contest: points}
            else:
                if contest in participants[username]:
                    if participants[username][contest] < points:
                        participants[username][contest] = points
                else:
                    participants[username][contest] = points
total_scores = {}
for i in participants:
    total_scores[i] = sum(participants[i].values())
    participants[i] = dict(sorted(participants[i].items(), key=lambda el: (el[1]), reverse=True))
participants = dict(sorted(participants.items(), key=lambda el: (el[0])))
total_scores = dict(sorted(total_scores.items(), key=lambda el: (el[1], el[0]), reverse=True))
top_performer = max(total_scores, key=total_scores.get)
top_points = total_scores[top_performer]
print(f"Best candidate is {top_performer} with total {top_points} points.")
print("Ranking:")
for i in participants:
    print(i)
    print_dictionary(participants[i], '#  {} -> {}')
