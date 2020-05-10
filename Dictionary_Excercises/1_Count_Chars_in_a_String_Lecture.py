def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dictionary(dictionary, separator):
    for k, v in dictionary.items():
        # print(f'{k} {separator} {v}')
        print(separator.format(k, v))


text = input()
text = text.replace(' ', '')
char_dict = {}
for ch in text:
    validate_key_existing(char_dict, ch)
    char_dict[ch] += 1

print_dictionary(char_dict, '{} -> {}')

# Other Way
# text = input()
# text = text.replace(' ', '')
# char_dict = {}
# for ch in text:
#     char_dict.setdefault(ch,0)
#     char_dict[ch] += 1
#
# print(char_dict)
