print("menghitung volume dan luas permukaan kerucut")
import math
t = int(input("masukan tinggi kerucut"))
r = int(input("masukan jari_jari_alasnya kerucut"))

s = math.sqrt(r**2+t**2)
phi = 3.141592

luas = (phi*r*s) + (phi*r*r)
volume = 1/3*phi*r*r*t

print("luas permukaan kerucut adalah ,: $",round(luas, 2))
print("volume kerucut adalah ,: $" ,round(volume, 2 ))

