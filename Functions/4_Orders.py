def prices(product,quantity):
    prices_dict = {'coffee': 1.5, 'water': 1, 'coke': 1.4, 'snacks': 2}
    print(f'{quantity * float(prices_dict[product]):.2f}')


product_name = input()
quantity = int(input())
prices(product_name,quantity)
