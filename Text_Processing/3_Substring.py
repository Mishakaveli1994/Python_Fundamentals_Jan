find_word = input()
string = input()
while find_word in string:
    string = string.replace(find_word,'')
print(string)