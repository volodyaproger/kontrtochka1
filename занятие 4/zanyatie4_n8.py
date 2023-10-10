n = int(input("Введите натуральное число меньше девяти"))
if 1 <= n <= 9:
    for a in range(1, n + 1):
        for b in range(1, a + 1):
            print(b, end="")
        print()
else:
    print("Ошибка")