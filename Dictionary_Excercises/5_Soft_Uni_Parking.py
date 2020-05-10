parking_lot_dict = {}
number_of_commands = int(input())
for i in range(number_of_commands):
    command_split = input().split(' ')

    if command_split[0] == 'register':
        username, license_plate = command_split[1], command_split[2]
        if username not in parking_lot_dict:
            parking_lot_dict[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_lot_dict[username]}")


    elif command_split[0] == 'unregister':
        username = command_split[1]
        if username not in parking_lot_dict:
            print(f"ERROR: user {username} not found")
        else:
            del parking_lot_dict[username]
            print(f"{username} unregistered successfully")

[print(f"{username} => {reg_num}") for username, reg_num in parking_lot_dict.items()]
