company_dict = {}

while True:
    command = input()
    if command == 'End':
        break
    else:
        command_split = command.split(' -> ')
        company, user = command_split[0], command_split[1]
        if company not in company_dict:
            company_dict[company] = [user]
        else:
            if user not in company_dict[company]:
                company_dict[company] += [user]
company_dict_sorted = {k: v for k, v in sorted(company_dict.items(), key=lambda x: x[0])}
for i, v in company_dict_sorted.items():
    print(i)
    [print(f'-- {b}') for b in v]
