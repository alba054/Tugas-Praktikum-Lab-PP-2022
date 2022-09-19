#Najwa Hanana
#H071221046
#menghitung volume dan luas permukaan kerucut

print ('---Menghitung Volume dan Luas Kerucut---')
print ('   ----------------------------------')
print ("Diketahui :")
r = int(input("Jari-jari Kerucut : "))
t = int(input("Tinggi Kerucut    : ")) 

phi=22/7

import math
# s = (round(math.sqrt(r**2+t**2), 2))
s = round((r ** 2 + t ** 2) ** (1/2), 2)

volume = (phi * r **2*t) / 3
lp = (phi * r * s)+(phi * r ** 2)

print()
print ("Volume Kerucut adalah         : ",round(volume,2)) 
print ("Luas Permukaan Kerucut adalah : ",round(lp,2))