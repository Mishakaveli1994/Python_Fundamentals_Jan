import time

number = int(input())
start_time = time.time()

# SoftUni version -> Faster
for num in range(1, number + 1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)
    # if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
    #     print(f'{num} -> True')
    # else:
    #     print(f'{num} -> False')
print("--- %s seconds --- Soft Uni Version" % (time.time() - start_time))
start_time = time.time()
# My Version
# for num in range(1, number + 1):
#     sum_of_digits = 0
#     for i in str(number):
#         sum_of_digits += int(i)
#     if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
#         print(f'{num} -> True')
#     else:
#         print(f'{num} -> False')
#
# print("--- %s seconds --- My Version" % (time.time() - start_time))
