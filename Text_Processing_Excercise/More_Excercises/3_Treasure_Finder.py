key = [int(i) for i in input().split(' ')]
counter = 0
treasure_maps = []
while True:
    text = input()
    if text == 'find':
        break
    else:
        counter = 0
        deciphered_text = ''
        for i in text:
            if counter == len(key):
                counter = 0
            shifted_chr = ord(i) - key[counter]
            deciphered_text += chr(shifted_chr)
            counter += 1
        treasure_maps.append(deciphered_text)
for i in treasure_maps:
    b = i.index('&')+1
    e = i[b:].index('&')+ b
    resource = i[b:e]
    b_l = i.index('<')+1
    e_l = i[b_l:].index('>')+ b_l
    location = i[b_l:e_l]
    print(f"Found {resource} at {location}")