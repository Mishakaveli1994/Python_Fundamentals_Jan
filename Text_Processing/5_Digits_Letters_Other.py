text = input()
types = {'digits': [], 'letters': [], 'other': []}
for i in text:
    if i.isdigit():
        types['digits'] += i
    elif i.isalpha():
        types['letters'] += i
    else:
        types['other'] += i
for i in types.values():
    print(''.join(i))
