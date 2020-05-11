import re

number_of_bosses = int(input())
boss_regex = r'\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#'
for i in range(number_of_bosses):
    boss_name = input()
    boss_stats = re.findall(boss_regex,boss_name)
    if len(boss_stats) == 1:
        boss_nick,boss_title = boss_stats[0]
        print(f"{boss_nick}, The {boss_title}")
        print(f">> Strength: {len(boss_nick)}")
        print(f">> Armour: {len(boss_title)}")
    else:
        print('Access denied!')