#1
A = int(input())
B = int(input())
if A < B:
    for num in range(A, B + 1):
        print(num)

#2
A = int(input())
B = int(input())
if A < B:
    for num in range(A, B + 1):
        print(num)
else:
    for num in range(A, B - 1, -1):
        print(num)


#3
A = int(input())
B = int(input())
for i in range(A - (A + 1) % 2, B - B % 2, 2):
    print(i)

#4
N = int(input())
summa = 0
for a in range(N):
    summa += int(input())
print(summa)

#5
N = int(input())
summa = 0
for num in range(1, N + 1):
    summa += num ** 3
print(summa)

#6
n = int(input())
otvet = 1
for a in range(1, n +1):
    otvet *= a
print(otvet)

#7
n = int(input())
for a in range(1, n + 1):
    for b in range(1, a + 1):
        print(b, sep='', end='')
    print()

#8
n = int(input("Введите натуральное число меньше девяти"))
if 1 <= n <= 9:
    for a in range(1, n + 1):
        for b in range(1, a + 1):
            print(b, end="")
        print()
else:
    print("Ошибка")

#9
def sumfib(n, s=0, c=0, p=1):
    if n == 0:
        return s
    return sumfib(n-1,s+c+p, c+p,c)

n =int(input("n="))
print(sumfib(n))