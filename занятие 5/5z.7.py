pred = int(input())
ans = 0
while pred != 0:
    next = int(input())
    if next != 0 and pred < next:
        ans += 1
    pred = next
print(ans)