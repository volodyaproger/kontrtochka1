def F(a, b, c):
    if a == b and a == c and c == b:
        print('3')
    elif (a == b and a == c) or (b == a and b == c) or (c == a and c == b):
        print('2')
    else:
        print('0')

a = input()
b = input()
c = input()

F(a, b, c)
