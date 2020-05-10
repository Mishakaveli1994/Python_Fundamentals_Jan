def pass_validation(string):
    digits = sum(c.isdigit() for c in string)
    letters = sum(c.isalnum() for c in string)
    checks = 3
    if not 6 <= len(string) <= 10:
        print("Password must be between 6 and 10 characters")
        checks -= 1
    if not len(string) == letters:
        print("Password must consist only of letters and digits")
        checks -= 1
    if not digits >= 2:
        print("Password must have at least 2 digits")
        checks -= 1
    if checks == 3:
        print("Password is valid")

pass_validation(input())