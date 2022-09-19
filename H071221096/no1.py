h = float(input("h : "))
a = float(input("a : "))
b = float(input("b : "))

import math
x = math.tan(b)*h
y = math.tan(a)*h
pk = y - x

print(round(pk , 5), "m")
print(pk , "m") 