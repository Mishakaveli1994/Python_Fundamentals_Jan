import re

number_of_registrations = int(input())
username_regex = r'(?<=U\$)[A-Z][a-z]{2,}(?=U\$)'
password_regex = r'(?<=P@\$)[A-Za-z]{5,}\d+(?=P@\$)'
successful_registrations = 0

for i in range(number_of_registrations):
    registration = input()
    username = re.findall(username_regex, registration)
    password = re.findall(password_regex, registration)
    if len(username) > 0 and len(password) > 0:
        print("Registration was successful")
        print(f"Username: {username[0]}, Password: {password[0]}")
        successful_registrations +=1
    else:
        print("Invalid username or password")
print(f'Successful registrations: {successful_registrations}')