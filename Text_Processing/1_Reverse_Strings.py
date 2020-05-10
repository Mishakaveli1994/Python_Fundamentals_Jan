while True:
    text = input()
    if text == 'end':
        break
    else:
        reverse_text = text[::-1]
        print(f"{text} = {reverse_text}")
