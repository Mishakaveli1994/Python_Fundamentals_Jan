char1 = ord(input())
char2 = ord(input())
random_string = input()
sums = 0
for i in random_string:
    if min(char1, char2) < ord(i) < max(char1, char2):
        sums += ord(i)
print(sums)
