a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("3")
if (a == b and a != c) or (b == c and  b != a) or (a == c and b != c):
    print("2")
if a != b != c:
    print("0")