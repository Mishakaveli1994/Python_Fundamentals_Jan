def reverse(s):
    return ''.join(reversed(s))


def main():
    result = {}

    while True:
        s = input()
        if s == 'end':
            break
        result[s] = reverse(s)

    for i, v in result.items():
        print(f"{i} = {v}")


if __name__ == '__main__':
    main()
