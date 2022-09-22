from math import tan, radians


h = int(input("masukkan h : "))
a = int (input("masukkan a : "))
b = int (input ("masukkan b : "))
a = radians (a)
b = radians (b)
x = tan(b) * h 
y = tan(a) * h
pk = round (y-x, 1)
print(pk, 'm')