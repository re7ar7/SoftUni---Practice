budget = float(input())
flour_price_for_one_kilo = float(input())
colored_eggs_total = 0
breads_quantity = 0
counter = 0

eggs_one_pack_price = flour_price_for_one_kilo * 0.75
liter_milk_price = flour_price_for_one_kilo + (flour_price_for_one_kilo * 0.25)
milk_needed_for_recipe = liter_milk_price / 4


loaf_of_bread_price = flour_price_for_one_kilo + eggs_one_pack_price + milk_needed_for_recipe

while budget >= loaf_of_bread_price:
    counter += 1
    breads_quantity += 1
    budget -= loaf_of_bread_price

    colored_eggs_total += 3

    if counter % 3 == 0:
        colored_eggs_total = colored_eggs_total - (breads_quantity - 2)


print(f'You made {breads_quantity} loaves of Easter bread! Now you have {colored_eggs_total} eggs and {budget:.2f}BGN left.')


