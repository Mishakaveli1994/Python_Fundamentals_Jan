n = int(input())
p = int(input())
mask = ~(1 << p)
number = n & mask
print(number)
