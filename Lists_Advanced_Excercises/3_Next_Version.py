version_number = input().split('.')
new_version = str(int(''.join(version_number))+1)
print('.'.join(new_version))