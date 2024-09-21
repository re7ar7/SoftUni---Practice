n = int(input())

sum = 0
for i in range(n):
    symbol = input()
    sum += ord(symbol)

print(f'The sum equals: {sum}')