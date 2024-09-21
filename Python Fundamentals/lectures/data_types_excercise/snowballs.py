n = int(input()) # number of snowballs
snowball_value = 0
highest_value = 0
for snowball in range(n):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality = int(input())

    snowball_value = (weight_of_snowball / time_needed) ** quality

    if snowball_value > highest_value:
        highest_value = snowball_value
        highest_weight = weight_of_snowball
        highest_time = time_needed
        highest_quality = quality

print(f'{highest_weight} : {highest_time} = {int(highest_value)} ({highest_quality})')
