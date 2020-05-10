morse_code_dict = {'.-': 'A',
                   '-...': 'B',
                   '-.-.': 'C',
                   '-..': 'D',
                   '.': 'E',
                   '..-.': 'F',
                   '--.': 'G',
                   '....': 'H',
                   '..': 'I',
                   '.---': 'J',
                   '-.-': 'K',
                   '.-..': 'L',
                   '--': 'M',
                   '-.': 'N',
                   '---': 'O',
                   '.--.': 'P',
                   '--.-': 'Q',
                   '.-.': 'R',
                   '...': 'S',
                   '-': 'T',
                   '..-': 'U',
                   '...-': 'V',
                   '.--': 'W',
                   '-..-': 'X',
                   '-.--': 'Y',
                   '--..': 'Z'}
text_deciphered = ''
current_word = ''
morse_text = [i for i in input().split(' ') if i != '']

for i in morse_text:
    if i == '|':
        text_deciphered += current_word
        text_deciphered += ' '
        current_word = ''
    else:
        current_word += morse_code_dict[i]
text_deciphered += current_word
print(text_deciphered)