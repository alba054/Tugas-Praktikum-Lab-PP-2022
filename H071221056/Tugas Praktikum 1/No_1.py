print("mencari panjang kapal")
import math
h = int(input("masukkan tinggi menara"))
a = int(input("masukkan sudut elavasi p terhadap ud kapal"))
b = int(input("masukkan sudut elevasi p terhadap ub kapal"))

xy = ('panjang dari belakang kapal ke menara')
qy = ('panjang dari depan kapal kemenara')

xy = math.tan(math.radians(a))*h
qy = math.tan(math.radians(b))*h

panjang_kapal= xy-qy

print("panjang kapal adalah ",round(panjang_kapal, 1))

