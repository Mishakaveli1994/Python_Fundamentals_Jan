string_input = input().split(', ')
indices_list = []

for i, x in enumerate(string_input):
    if int(x) % 2 == 0:
        indices_list.append(int(i))
print(indices_list)