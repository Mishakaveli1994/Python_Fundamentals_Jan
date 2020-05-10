products = {}

while True:
    product = input()
    if product == 'statistics':
        print('Products in stock:')
        for i in products:
            print(f'- {i}: {products[i]}')
        print(f'Total Products: {len(products.keys())}')
        print(f'Total Quantity: {sum(products.values())}')
        break
    else:
        product_split = product.split(': ')
        product_name = product_split[0]
        product_quantity = int(product_split[1])
        if product_name not in products:
            products[product_name] = product_quantity
        else:
            products[product_name] += product_quantity
