def user_length(user):
    valid = 1
    if 3 <= len(user) <= 16:
        valid = 0
    return valid


def forbidden_symbols(user):
    allowed = ['-', '_']
    valid = 0
    for i in user:
        if i.isalnum() or i in allowed:
            pass
        else:
            valid = 1
    return valid


def redundant_symbols(user):
    valid = 0
    if ' ' in user:
        valid = 1
    return valid


usernames = input().split(', ')
for i in usernames:
    check = 0
    check += user_length(i)
    check += forbidden_symbols(i)
    check += redundant_symbols(i)
    if check == 0:
        print(i)
