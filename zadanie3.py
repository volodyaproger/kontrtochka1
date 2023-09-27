#1
x = int(input())
y = int(input())
z = int(input())
print("Сумма:", x + y + z)

#2
a = int(input())
b = int(input())
print((a * b) / 2)

#3
n = int(input())
if n / 60 <= 24:
    print("Часы:", n // 60, "Минуты:", n % 60)
else:
    print("Количество введенных минут больше, чем минут в сутки")

#4
a = int(input())
b = int(input())
l = int(input())
N = int(input())
print(2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)

#5
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

#6
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 + b1) % 2 == (a2 + b2) % 2:
    print("ДА")
else:
    print("НЕТ")

#7
year = int(input())
if (year % 4 == 0 and year%100 != 0) or (year%400 == 0):
    print("Год високосный")
else:
    print("Год обычный")

#8
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("3")
if (a == b and a != c) or (b == c and  b != a) or (a == c and b != c):
    print("2")
if a != b != c:
    print("0")