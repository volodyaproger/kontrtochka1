from math import prod
lIst = list(map(int, input().split()))
print(sum(lIst[i] for i in range(1, len(lIst), 2)))
print(prod(lIst[j] for j in range(0, len(lIst), 2)))