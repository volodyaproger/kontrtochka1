def F(n, div=2):
    if n < 2:
        return False
    if div * div > n:
        return True
    if n % div == 0:
        return False
    return F(n, div + 1)

n = int(input("Введите натуральное число больше 1: "))

if F(n):
    print("YES")
else:
    print("NO")
