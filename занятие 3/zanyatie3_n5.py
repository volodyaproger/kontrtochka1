a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
min = 0
if a < b:
    if a < c:
        min = a
    else:
        min = c
else:
    if b < c:
        min = b
    else:
        min = c
print("Минимальное число:", min)
