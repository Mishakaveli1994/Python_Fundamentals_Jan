initial_email = input()

while True:
    command = input()
    if command == 'Complete':
        break
    else:
        command_split = command.split(' ')
        if command_split[0] == 'Make':
            if command_split[1] == 'Upper':
                initial_email = initial_email.upper()
                print(initial_email)
            elif command_split[1] == 'Lower':
                initial_email = initial_email.lower()
                print(initial_email)
        elif command_split[0] == 'GetDomain':
            print(initial_email[len(initial_email) - int(command_split[1]):])
        elif command_split[0] == 'GetUsername':
            if '@' in initial_email:
                at_index = initial_email.index('@')
                print(initial_email[0:at_index])
            else:
                print(f"The email {initial_email} doesn't contain the @ symbol.")
        elif command_split[0] == 'Replace':
            initial_email = initial_email.replace(command_split[1], '-')
            print(initial_email)
        elif command_split[0] == 'Encrypt':
            val = ([str(ord(i)) for i in initial_email])
            print(' '.join(val))