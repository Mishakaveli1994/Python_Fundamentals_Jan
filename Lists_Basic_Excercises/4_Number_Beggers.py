numbers = input().split(', ')
number_of_beggars = int(input())
taken = [0] * number_of_beggars

while True:
    if len(numbers) == 0:
        break
    else:
        for i in range(number_of_beggars):
            if len(numbers) == 0:
                break
            else:
                taken[i] += int(numbers[0])
                numbers.pop(0)
print(taken)