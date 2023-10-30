def F(n):
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a

def F1(n):
    b = 0
    for i in range(1, n + 1):
        b += F(i)
    return b

n = int(input('Введите число:'))
a = F1(n)
print(a)
