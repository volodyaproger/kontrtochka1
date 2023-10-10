def sumfib(n, s=0, c=0, p=1):
    if n == 0:
        return s
    return sumfib(n-1,s+c+p, c+p,c)

n =int(input("n="))
print(sumfib(n))