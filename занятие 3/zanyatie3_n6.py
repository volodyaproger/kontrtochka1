def F(a1, a2, b1, b2):
    c1 = 0
    c2 = 0
    if a1 or a2 %2==0:
        c1 = 1
    else:
        c1 = 0
    if b1 or b2 %2==0:
        c2 = 1
    else:
        c2 = 0
    if c1 == c2:
        print('ДА')
    else:
        print('НЕТ')

a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

F(a1, a2, b1, b2)
