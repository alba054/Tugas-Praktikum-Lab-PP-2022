print("Menghitung Panjang Kapal")

h = float(input("Ketinggian menara : "))
a = int(input("Sudut elevasi belakang kapal : "))
b = int(input("Sudut elevasi depan kapal : "))

import math

rad = (math.pi/180)*a
tan_a = math.tan(rad)

rad = (math.pi/180)*b
tan_b = math.tan(rad)

ac= tan_a*h
bc= tan_b*h

ab = float(ac-bc)

print("Panjang kapal = ", round(ab,1), 'm')