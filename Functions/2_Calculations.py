def calculate(operator, int_1, int_2):
    functions = {'multiply': '*', 'divide': '/', 'add': '+', 'subtract': '-'}
    result = (eval(f'{int_1}{functions[operator]}{int_2}'))
    print(int(result))
operator = input()
integer_1 = input()
integer_2 = input()

calculate(operator,integer_1,integer_2)