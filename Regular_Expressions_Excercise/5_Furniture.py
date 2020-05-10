import re
total_price = 0
items = []
regex = r"(>>([a-zA-Z]+)<<([\d]+[.]?[\d]+)!(\d+))"
while True:
    item = input()
    if item == 'Purchase':
        break
    else:
        match = re.findall(regex, item)
        if len(match) > 0:
            total_price += float(match[0][2]) * float(match[0][3])
            items.append(match[0][1])
print(f"Bought furniture:")
for i in items:
    print(i)
print(f"Total money spend: {total_price:.2f}")