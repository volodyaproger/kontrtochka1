def F(n):
    if 1 <= n <= 9:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()  
    else:
        print("Ошибка")

n = int(input())

F(n)
