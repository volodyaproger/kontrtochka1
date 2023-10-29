x = int(input('Введите число:'))
y = int(input('Введите число:'))
day_number = 1
while x < y:
    x *= 1.1
    day_number += 1
print(day_number)
