def get_letter_position(letter):
    num = 96
    if letter.isupper():
        num = 64
    return ord(letter) - num


strings = input().split()
sums = 0
for i in strings:
    first_letter = i[0]
    last_letter = i[-1]
    number = int(i[1:len(i) - 1])
    if first_letter.islower():
        number *= get_letter_position(first_letter)
    else:
        number /= get_letter_position(first_letter)
    if last_letter.isupper():
        number -= get_letter_position(last_letter)
    else:
        number += get_letter_position(last_letter)
    sums += number
print(f"{sums:.2f}")
