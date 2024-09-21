orders_quantity = int(input())
total_sum = 0


for i in range(orders_quantity):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if 0.01 > price_per_capsule or price_per_capsule > 100:
        continue
    elif 1 > days or days > 31:
        continue
    elif 1 > capsules_needed_per_day or capsules_needed_per_day > 2000:
        continue


    current_coffee_price = price_per_capsule * days * capsules_needed_per_day
    total_sum += current_coffee_price

    if current_coffee_price > 0:
        print(f'The price for the coffee is: ${current_coffee_price:.2f}')

print(f'Total: ${total_sum:.2f}')
