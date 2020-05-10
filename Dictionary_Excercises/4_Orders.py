product_dict = {}

while True:
    product = input()
    if product == 'buy':
        break
    else:
        product_split = product.split(' ')
        product_name = product_split[0]
        product_price = float(product_split[1])
        product_quantity = int(product_split[2])
        if product_name not in product_dict:
            product_dict[product_name] = {'price': product_price, 'quantity': product_quantity}
        else:
            product_dict[product_name]['quantity'] += product_quantity
            product_dict[product_name]['price'] = product_price

for i in product_dict.keys():
    print(f"{i} -> {product_dict[i]['quantity']*product_dict[i]['price']:.2f}")

# [print(f"{name} -> {product_dict[name]['quantity']*product_dict[name]['price']:.2f}") for name in product_dict.keys()]