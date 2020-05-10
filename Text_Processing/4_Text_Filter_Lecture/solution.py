def solution(banned_words, text):
    for banned_word in banned_words:
        text = text.replace(banned_word, '*' * len(banned_word))
    return text


if __name__ == '__main__':
    banned_words = input().split(', ')
    text = input()
    print(solution(banned_words, text))
