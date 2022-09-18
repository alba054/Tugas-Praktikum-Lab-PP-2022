import math 
h = float(input('tinggi menara='))
a = float(input('sudut elevasi terhadap ujung depan kapal='))
b = float(input('sudut elevasi terhadap ujung belakang kapal='))

total_panjang = math.tan(math.radians(a))*h
jarak_kapal_menara = math.tan(math.radians(b))*h
panjang_kapal = total_panjang-jarak_kapal_menara

print ('panjang kapal adalah', round(panjang_kapal, 1))