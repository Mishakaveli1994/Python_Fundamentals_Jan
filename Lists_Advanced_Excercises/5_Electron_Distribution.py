electrons = int(input())
electron_distribution = []

while electrons > 0:
    if electrons > 2 * ((len(electron_distribution) + 1) ** 2):
        electron_distribution.append(2 * ((len(electron_distribution) + 1) ** 2))
        electrons -= 2 * (len(electron_distribution) ** 2)
    else:
        electron_distribution.append(electrons)
        electrons = 0
print(electron_distribution)
