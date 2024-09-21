n = int(input())
tank_capacity = 255


for i in range(n):

    water_poured = int(input())

    if tank_capacity - water_poured < 0:
        print('Insufficient capacity!')
        continue
    else:
        tank_capacity -= water_poured


print(255 - tank_capacity)

