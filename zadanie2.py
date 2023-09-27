#1
import math
x = 3.74*10**(-2)
y = -0.825
z = 0.16*10**2
s = ((1 + (math.sin(x + y))**2)/abs(x - (2*y)/(1 + x**2 * y**2))) * x**abs(y) + (math.cos(math.atan(1/z)))**2
print(s)
#s=1,05534

#2
from math import *
x = -4.5
y = 0.75*10**(-4)
z = -0.845*10**2
s = (((9+((x-y)**2)) ** (1./3.)) / (x**2 + y**2 + 2)) - (exp(abs(x-y)) * tan(z)**3)
print(s)
#s=-3,23765

#3
from math import *
x = 3.74*10**(-2)
y = -0.825
z = 0.16*10**2

s = ((1 + (sin(x + y))**2)/abs(x - (2*y)/(1 + x**2 * y**2))) * x**abs(y) + (cos(atan(1/z)))**2
print(s)
#s=1,05534