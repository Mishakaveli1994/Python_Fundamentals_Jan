def palindrome_integers(number_list):
    for i in number_list:
        value = int(i)
        if i == str(value)[::-1]:
            print('True')
        else:
            print('False')


lists = input().split(', ')
palindrome_integers(lists)
