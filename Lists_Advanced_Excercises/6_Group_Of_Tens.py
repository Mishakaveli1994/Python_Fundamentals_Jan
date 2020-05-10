numbers = [int(i) for i in input().split(', ')]
group = []
groups = 10

while True:
    if len(numbers) == 0:
        break
    group = [number for number in numbers if number <= groups]
    remove = [index for index,number in enumerate(numbers) if number <= groups]
    remove.sort()
    remove.reverse()
    for i in remove:
        numbers.pop(i)

    print(f"Group of {groups}'s: {group}")
    groups += 10

