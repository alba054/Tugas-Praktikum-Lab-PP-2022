print("Menghitung Luas dan Volume Kerucut")

r = int(input("Masukkan Jari-Jari ="))
t = int(input("Masukkan Tingginya ="))
la = int(input("Masukkan Luas Alas ="))
ls = int(input("Masukkan Luas Selimut ="))

phi = 22/7

volume = 1/3*(phi*r*r*t)
luas = la + ls 

print("Luas Kerucut Adalah =", luas)
print("Volume Kerucut Adalah =", volume)