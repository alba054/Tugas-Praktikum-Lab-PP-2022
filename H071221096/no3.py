r = float(input("jari_jari_alas = "))
t = float(input("tinggi = "))
s = float(input("garis pelukis = "))

volume = (1/3) * 3.14 * r**2 * t
luas_permukaan = (3.14 * r**2) + (3.14* r * s)

print ("> volume : " , round (volume , 2))
print ("> luas permukaan : " , round (luas_permukaan , 2))