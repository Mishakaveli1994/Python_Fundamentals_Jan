from io import StringIO


# StringIO operations
# Optimizes usage of memory as the string does not change it's memory address constantly
def repeat_by_length(string):
    s = StringIO()
    for _ in range(len(string)):
        s.write(string)
    s.seek(0)
    return s.read()


def repeat_each_word_by_length(words):
    s = StringIO()
    for word in words:
        s.write(repeat_by_length(word))
    s.seek(0)
    return s.read()


if __name__ == '__main__':
    words = input().split(' ')
    print(repeat_each_word_by_length(words))

# Normal Operations
# def repeat_by_length(string):
#     return string * len(string)
#
#
# def repeat_each_word_by_length(words):
#     s = ''
#     for word in words:
#         s += repeat_by_length(word)
#     return s
