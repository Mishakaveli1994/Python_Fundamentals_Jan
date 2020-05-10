type = input()
if type == 'int':
    integer = int(input())*2
    print(integer)
elif type == 'real':
    float_num = float(input())*1.5
    print(f'{float_num:.2f}')
elif type == 'string':
    string = input()
    print(f'${string}$')