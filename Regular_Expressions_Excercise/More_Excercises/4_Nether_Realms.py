import re

health_regex = r'[^0-9\.\+\-\*\/]'
mul_sub_regex = r'[\*\/]+'
damage_regex = r'[+|-]?\d+\.?\d*'
deamons = [i.strip() for i in input().split(',')]
deamon_dict = {}
for i in deamons:
    if ',' in i or len(re.findall(health_regex, i)) < 1:
        continue
    else:
        health = sum(int(ord(b)) for b in re.findall(health_regex, i))
        damage = sum(float(c) for c in re.findall(damage_regex, i))
        modifiers = ''.join(re.findall(mul_sub_regex, i))
        for e in modifiers:
            if e == '*':
                damage *= 2
            elif e == '/':
                damage /= 2
        deamon_dict[i] = [health, damage]
sorted_deamons = sorted(deamon_dict.items())
for i in sorted_deamons:

    print(f"{i[0]} - {i[1][0]} health, {i[1][1]:.2f} damage")