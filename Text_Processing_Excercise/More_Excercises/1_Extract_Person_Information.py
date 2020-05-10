number_of_data = int(input())
names = []
ages = []
for i in range(number_of_data):

    text = input()
    for index,value in enumerate(text):
        if value == '@':
            if text[index+1].isalpha():
                end_index = text[index:].index('|')
                names.append(text[index+1:end_index+index])
        if value == '#':
            if text[index + 1].isdigit():
                end_index = text[index:].index('*')
                ages.append(text[index + 1:end_index + index])
for i,v in zip(names,ages):
    print(f"{i} is {v} years old.")