h = int(input("Masukkan nilai h:"))
a = int(input('''Masukkan nilai sudut elevasi pengamat terhadap ujung belakang
kapal:'''))
b = int(input('''Masukkan sudut elevasi pengamat 
terhadap ujung depan kapal:'''))
import math
A = math.radians(a)
B = math.radians(b)
pB = h* math.tan (B)
pA = h* math.tan (A)
pk = pA-pB
print(round(pk,1))
#pK = math.radians(pk)
#print (round (pk,1))