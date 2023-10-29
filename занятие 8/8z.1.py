#У меня 7 вариант!
import math
x = float(input('x: '))
y = float(input('y: '))
z = float(input('z: '))
t = float(input('t: '))
d = math.sqrt(x*x + y*y)

def Quadrilateral1(x, y):
    return x*y*0.5

def Quadrilateral2(d, z, t):
    p = (z+t+d)/2
    return math.sqrt(p*(p-z)*(p-t)*(p-d))
print(Quadrilateral1(x, y) + Quadrilateral2(d, z, t))