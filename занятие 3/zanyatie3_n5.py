a = int(input())
b = int(input())
c = int(input())
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