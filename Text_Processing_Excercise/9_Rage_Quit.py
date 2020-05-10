from io import StringIO

text = input().upper()
complete_text = StringIO()
digits = ''
chars = ''
unique_chars = []
for i in range(len(text)):
    if not text[i].isdigit():
        chars += text[i]
    else:
        digits += text[i]
        if i == len(text) - 1:
            complete_text.write(chars * int(digits))
            if int(digits) > 0:
                for b in chars:
                    if b not in unique_chars:
                        unique_chars.append(b)
        else:
            if not text[i + 1].isdigit():
                complete_text.write(chars * int(digits))
                if int(digits) > 0:
                    for b in chars:
                        if b not in unique_chars:
                            unique_chars.append(b)
                digits = ''
                chars = ''
complete_text.seek(0)
print(f"Unique symbols used: {len(unique_chars)}")
print(complete_text.read())
