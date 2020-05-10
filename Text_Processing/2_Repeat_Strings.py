from io import StringIO

# Without StringIO
# strings = input().split(' ')
# new_string = ''
# for i in strings:
#     new_string += i * len(i)
# print(new_string)

# With StringIO
strings = input().split(' ')
new_string = StringIO()
for i in strings:
    new_string.write(i * len(i))
new_string.seek(0)
print(new_string.read())