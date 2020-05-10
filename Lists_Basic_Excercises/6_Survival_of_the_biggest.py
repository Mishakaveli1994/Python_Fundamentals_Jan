numbers = input().split(' ')
list_of_int = []
num_to_remove = int(input())
for i in numbers:
    list_of_int.append(int(i))

for i in range(num_to_remove):
    minimum = list_of_int.index(min(list_of_int))
    list_of_int.pop(minimum)

print(list_of_int)