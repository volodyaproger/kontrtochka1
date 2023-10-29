a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
if a == b == c:
    print("3")
if (a == b and a != c) or (b == c and  b != a) or (a == c and b != c):
    print("2")
if a != b != c:
    print("0")
