rows = int(input())
row_structure = [[['1', '1', '0', '0', '0']],
                 [['1', '1', '0', '0', '0']],
                 [['0', '0', '0', '0', '0']],
                 [['0', '0', '0', '0', '0']],
                 [['0', '0', '0', '1', '1']]]
bitten = []

# for i in range(rows):
#     row_struct = input().split(' ')
#     row_structure.append([row_struct])
# print(row_structure)

for i in row_structure:
    for b in i:
        if i == 1 and b == 1:
