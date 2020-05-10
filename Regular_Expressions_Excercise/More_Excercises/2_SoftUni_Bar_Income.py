import re

regex = r'(%[A-Z][a-z]+%)[^.%$|]*(<\w+>)[^.%$|]*(\|[\d]*\|)[^.%$|]*?([0-9]+\.?[0-9]*\$)'
# Better Version of the regex - %([A-Z][a-z]+)%[^.%$|]*<(\w+)>[^.%$|]*\|([\d]*)\|[^.%$|]*?([0-9]+\.?[0-9]*)\$
# To avoid the separator symbols in the group, put the them outside of the group when selecting

total_income = 0
while True:
    command = input()
    if command == 'end of shift':
        break
    else:

        find = list(re.findall(regex, command))
        if len(find) > 0:
            if len(find[0]) == 4:
                name_unref, product_unref, v, c = find[0]
                name = name_unref[1:len(find[0][0]) - 1]
                product = product_unref[1:len(find[0][1]) - 1]
                value = float(v[1:len(find[0][2]) - 1]) * float(c[:len(find[0][3]) - 1])
                total_income += value
                print(f"{name}: {product} - {value:.2f}")

print(f'Total income: {total_income:.2f}')
