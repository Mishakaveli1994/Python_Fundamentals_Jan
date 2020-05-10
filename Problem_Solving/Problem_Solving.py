import sys

# Brute Force Approach
# mass1 = [54, 43, 11, -1, 45, 12, 7, 11]
# mass2 = [84, 123, 14, 45, 5, 27, 6]
# target = 15
# closest = sys.maxsize
# closest_numbers = []
# for i in mass1:
#     for b in mass2:
#         if abs(target-(i + b)) < closest:
#             closest = abs(target-(i + b))
#             closest_numbers = [i, b]
# print(closest_numbers)

# SoftUni Sheet Approach
mass1 = [1, 8, 5]
mass2 = [4, 9, 2]
target = 7


def solve(firstArr, secondArr, target):
    firstArr.sort()
    secondArr.sort()
    x = len(firstArr) - 1
    y = 0
    minDiff = sys.maxsize
    result = []
    while x > 0 and y < len(secondArr):
        sum = abs(firstArr[x] + secondArr[y])
        diff = abs(sum - target)

        if diff < minDiff:
            result = [firstArr[x], secondArr[y]]
            minDiff = diff

        if sum >= target:
            x -= 1
        else:
            y += 1
    print(result)


solve(mass1, mass2, target)
