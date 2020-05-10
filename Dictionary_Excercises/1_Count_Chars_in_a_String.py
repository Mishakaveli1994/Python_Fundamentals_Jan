text = input()
char_dict = {}
for i in text:
    if i != ' ':
        if i not in char_dict:
            char_dict[i] = 0
        char_dict[i] += 1
[print(f"{key} -> {value}") for key, value in char_dict.items()]
