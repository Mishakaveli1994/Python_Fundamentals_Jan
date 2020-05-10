from io import StringIO

def shift_letter(text):
    encoded_text = StringIO()
    for i in text:
        ori = ord(str(i))
        changed = chr(ori+3)
        encoded_text.write(changed)
    encoded_text.seek(0)
    return encoded_text.read()

original_text = input()
encrypted = shift_letter(original_text)
print(encrypted)