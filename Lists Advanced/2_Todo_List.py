todos_ul = []
while True:
    todos = input()
    if todos == 'End':
        break
    else:
        todos_ul.append(todos)

todos_ul.sort(key=lambda fname: int(fname.split('-')[0]))
todos_ol = [x[x.index('-')+1:] for x in todos_ul]
print(todos_ol)
