def factorial(list):
    factorial_list = []
    for i in list:
        factorial = 1
        for b in range(1,i+1):
            factorial *= b
        factorial_list.append(factorial)
    print(f'{factorial_list[0]/factorial_list[1]:.2f}')

number_list = []
for i in range(2):
    number_list.append(int(input()))

factorial(number_list)
