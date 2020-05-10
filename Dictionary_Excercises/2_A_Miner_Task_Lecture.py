def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


def print_dictionary(dictionary, separator):
    for k, v in dictionary.items():
        print(separator.format(k, v))


resource_dict = {}

while True:
    resource = input()

    if resource == 'stop':
        break
    else:
        quantity = int(input())
        validate_key_existing(resource_dict, resource)
        resource_dict[resource] += quantity

print_dictionary(resource_dict, '{} -> {}')
