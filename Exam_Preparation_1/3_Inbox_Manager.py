def check_user(dictionary, username):
    if username not in dictionary:
        users[username] = []
    else:
        print(f"{username} is already registered")


def delete_user(dictionary, username):
    if username not in dictionary:
        print(f"{username} not found!")
    else:
        del users[username]


users = {}
while True:
    command = input()
    if command == 'Statistics':
        break
    else:
        command_split = command.split('->')
        if command_split[0] == 'Add':
            check_user(users, command_split[1])
        elif command_split[0] == 'Send':
            users[command_split[1]] += [command_split[2]]
        elif command_split[0] == 'Delete':
            delete_user(users, command_split[1])
sorted_users = dict(sorted(users.items(), key=lambda x: (-len(x[1]), x[0])))
print(f"Users count: {len(sorted_users)}")
for k,v in sorted_users.items():
    print(k)
    for i in v:
        print(f" - {i}")