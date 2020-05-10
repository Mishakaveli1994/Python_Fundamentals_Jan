def odd_and_even(num1):
    even = sum([int(i) for i in str(num1) if int(i) % 2 == 0])
    odd = sum([int(i) for i in str(num1) if int(i) % 2 != 0])
    return even,odd

integer = int(input())
even, odd = (odd_and_even(integer))
print(f'Odd sum = {odd}, Even sum = {even}', sep =',')