people_total = int(input())
elevator_capacity = int(input())

courses_total = 0

if elevator_capacity > people_total:
    print(1)
else:
    courses_total = people_total // elevator_capacity
    if people_total % elevator_capacity == 0:
        print(courses_total)
    else:
        courses_total += 1
        print(courses_total)

