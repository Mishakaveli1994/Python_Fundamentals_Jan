text = input()

for index, letter in enumerate(text):
    if letter == ':' and text[index + 1].isprintable():
        print(f"{letter}{text[index + 1]}")
       