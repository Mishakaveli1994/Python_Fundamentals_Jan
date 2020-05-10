elements = input().split(' ')
bakery = {}
for i in range(0,len(elements),2):
    key = elements[i]
    value = int(elements[i+1])
    bakery[key] = value

requests = input().split()

for i in requests:
    if i in bakery:
        print(f"We have {bakery[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")