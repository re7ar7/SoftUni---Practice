lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expanses = 0
count = 0

for fight in range(1, lost_fights_count +1):

    if fight % 2 == 0:
        expanses += helmet_price
    if fight % 3 == 0:
        expanses += sword_price
        if fight % 2 == 0:
            expanses += shield_price
            count += 1
            if count % 2 == 0:
                expanses += armor_price

print(f'Gladiator expenses: {expanses:.2f} aureus')

