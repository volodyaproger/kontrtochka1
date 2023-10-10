def S(a, b, l, N):
    dlina = 2 * (N - 1) * a + 2 * N * b + l
    return dlina
a = int(input())
b = int(input())
l = int(input())
N = int(input())
r = S(a, b, l, N)
print(r)