N = int(input())
dvoika = 2
step = 1
while dvoika <= N:
    dvoika *= 2
    step += 1
print(step - 1, dvoika // 2)