string = input()
file_name_index = string.rindex('\\',) + 1
file_list = string[file_name_index:].split('.')
print(f"File name: {file_list[0]}")
print(f"File extension: {file_list[1]}")