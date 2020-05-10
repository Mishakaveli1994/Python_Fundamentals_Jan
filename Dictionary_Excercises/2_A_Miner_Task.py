resources = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    else:
        quantity = int(input())
        if resource not in resources:
            resources[resource] = 0
        resources[resource] += quantity
[print(f"{key} -> {value}") for key, value in resources.items()]
