def find_second_larg(numbers):
    if len(numbers) == 0:
        return None
    max_num = max(numbers)
    numbers.remove(max_num)
    second_max = max(numbers)
    return second_max
numbers = []
while True:
    num = int(input("Введите число (0 для окончания ввода): "))
    if num == 0:
        break
    numbers.append(num)
second_larg = find_second_larg(numbers)
print("Второй по величине элемент:", second_larg)

input("Нажмите Enter для выхода")
