def sum_numbers(int1, int2):
    sums = int1 + int2
    return sums


def subtract_numbers(sum_num, num3):
    sub = sum_num - num3
    return sub


def add_and_subtract(int1, int2, int3):
    sums = sum_numbers(int1, int2)
    print(subtract_numbers(sums, int3))


int1 = int(input())
int2 = int(input())
int3 = int(input())

add_and_subtract(int1, int2, int3)
