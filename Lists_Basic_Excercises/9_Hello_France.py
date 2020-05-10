items = input().split('|')
budget = float(input())
bought_items = []
new_prices = []
profit = 0

item_types = {'Clothes': 50, 'Shoes': 35, 'Accessories': 20.5}

for item in items:
    item = item.split("->")
    price = float(item[1])
    name = item[0]
    if (price <= item_types[name]) and budget >= price:
        bought_items.append(price)
        y1 = f'{(price * 1.4):.2f}'
        new_prices.append(str(y1))
        budget -= price
profit = sum([float(x) for x in new_prices])

print(*new_prices)
print(f"Profit: {profit- sum(bought_items):.2f}")
if (budget + profit) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")