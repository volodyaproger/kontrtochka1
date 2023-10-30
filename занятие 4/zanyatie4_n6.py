def F(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    print(a)

n = int(input())

F(n)
