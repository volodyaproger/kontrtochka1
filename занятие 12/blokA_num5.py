def obr_por(n):
    if n < 10:
        print(n)
    else:
        obr_por(n // 10)
        print(n % 10)
n = int(input("Введите натуральное число: "))

print("Цифры числа N:")
obr_por(n)
