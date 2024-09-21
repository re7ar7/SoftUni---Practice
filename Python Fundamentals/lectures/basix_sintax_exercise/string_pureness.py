strings_quantity = int(input())

for i in range(strings_quantity):
    command = input()
    if "," in command or '.' in command or '_' in command:
        print(f'{command} is not pure!')

    else:
        print(f'{command} is pure.')