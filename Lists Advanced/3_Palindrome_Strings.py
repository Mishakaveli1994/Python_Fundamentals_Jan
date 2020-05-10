string_input = input().split(' ')
palindrome = input()
times_found = 0
palindrome_list = []

for i in string_input:
    if palindrome == i[::-1]:
        times_found+=1
    if i == i[::-1]:
        palindrome_list.append(i)

print(palindrome_list)
print(f'Found palindrome {times_found} times')