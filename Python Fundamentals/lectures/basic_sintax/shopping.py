budget = int(input())
total_sum = 0

while True:
    command = input()

    if command == 'End':
        print('You bought everything needed.')
        break

    total_sum += float(command)

    if total_sum > budget:
        print('You went in overdraft!')
        break
