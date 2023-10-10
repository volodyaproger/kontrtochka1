A = int(input())
B = int(input())
for i in range(A - (A + 1) % 2, B - B % 2, 2):
    print(i)