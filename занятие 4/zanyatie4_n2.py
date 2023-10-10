A = int(input())
B = int(input())
if A < B:
    for num in range(A, B + 1):
        print(num)
else:
    for num in range(A, B - 1, -1):
        print(num)