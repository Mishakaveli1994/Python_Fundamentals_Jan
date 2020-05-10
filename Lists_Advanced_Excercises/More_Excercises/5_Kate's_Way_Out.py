maze_rows = int(input())
maze_structure = []
for i in range(4):
    maze_structure.append([i for i in input()])

# for index,value in enumerate(maze_structure):
#     if 'k' in value:
#         kate_location = [index,value.index('k')]
for rows in maze_structure:
    for lines in rows:
        print(rows,lines)