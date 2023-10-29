summa = 0
len = 0
number = int(input())
while number != 0:
    summa += number
    len += 1
    number = int(input())
print(summa / len)