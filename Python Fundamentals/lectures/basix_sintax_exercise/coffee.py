
command = input()
coffees_quantity = 0

while command != 'END':
    if command == 'coding' or command =='cat' or command == 'dog' or command =='movie' \
            or command == 'CODING' or command =='CAT' or command == 'DOG' or command =='MOVIE':
        if command.islower():
            coffees_quantity += 1
        else:
            coffees_quantity += 2

    command = input()


if coffees_quantity > 5:
    print(f'You need extra sleep')
else:
    print(coffees_quantity)

