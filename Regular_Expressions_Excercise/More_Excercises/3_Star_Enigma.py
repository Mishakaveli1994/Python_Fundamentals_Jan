import re

regex = r'[starSTAR]'
regex_decr = r'((?<=@)[a-zA-Z]+)[^@\-!:>]*:([\d]+)[^@\-!:>]*!([A,D])![^@\-!:>]*->(\d+)'
number_of_commands = int(input())
planets = {'Destroyed': [], 'Attacked': []}
for i in range(number_of_commands):
    command = input()
    index = re.findall(regex, command)
    index_len = len(index)
    decrypted_command = ''.join([chr(ord(b) - index_len) for b in command])
    decrypted_command = re.findall(regex_decr, decrypted_command)
    if len(decrypted_command) > 0:
        if len(decrypted_command[0]) == 4:
            planet_name = decrypted_command[0][0]
            type_of_attack = decrypted_command[0][2][0]
            if type_of_attack == 'D':
                planets['Destroyed'].append(planet_name)
            elif type_of_attack == 'A':
                planets['Attacked'].append(planet_name)
planets['Destroyed'] = sorted(planets['Destroyed'])
planets['Attacked'] = sorted(planets['Attacked'])

print(f"Attacked planets: {len(planets['Attacked'])}")
for i in planets['Attacked']:
    print(f"-> {i}")

print(f"Destroyed planets: {len(planets['Destroyed'])}")
for i in planets['Destroyed']:
    print(f"-> {i}")