courses_dict = {}
while True:
    command = input()
    if command == 'end':
        break
    else:
        command_split = command.split(' : ')
        course = command_split[0]
        student = command_split[1]
        if course not in courses_dict:
            courses_dict[course] = [student]
        else:
            courses_dict[course] += [student]
sorted_dict = sorted(courses_dict.items(), key=lambda x: (-len(x[1])))
for i in sorted_dict:
    print(f"{i[0]}: {len(i[1])}")
    for b in sorted(i[1]):
        print(f"-- {b}")