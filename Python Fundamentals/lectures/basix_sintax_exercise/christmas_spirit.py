decorations_quantity = int(input())
days = int(input()) # untill Xmas

christmas_spirit_total = 0
money_spent_total = 0
                     #xmax spirit points
ornament_set = 2       # 5
tree_skirt = 5          # 3
tree_garland = 3       # 10
tree_lights = 15       #17


for current_day in range(1, days + 1):

    if current_day % 11 == 0:
        decorations_quantity += 2
    if current_day % 2 == 0:
        money_spent_total += decorations_quantity * ornament_set
        christmas_spirit_total += 5
    if current_day % 3 == 0:
        money_spent_total += decorations_quantity * (tree_skirt + tree_garland)
        christmas_spirit_total += 13
    if current_day % 5 == 0:
        money_spent_total += decorations_quantity * tree_lights
        christmas_spirit_total += 17
        if current_day % 3 == 0:
            christmas_spirit_total += 30
    if current_day % 10 == 0:
        christmas_spirit_total -= 20
        money_spent_total += tree_skirt + tree_garland + tree_lights

if days % 10 == 0:
    christmas_spirit_total -=30


print(f'Total cost: {money_spent_total}')
print(f'Total spirit: {christmas_spirit_total}')
