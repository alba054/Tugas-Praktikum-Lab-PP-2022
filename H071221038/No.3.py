print("Menghitung Volume dan Luas Permukaan Kerucut")

phi = 3.14
r = int(input("Masukkan jari-jari alas kerucut : "))
s = int(input("Masukkan nilai selimut kerucut : "))
t = int(input("Masukkan tinggi kerucut : "))

luas = phi*r*(s+r)
volume = 1/3*phi*r**2*t

print("Volume kerucut = ", round(volume,2))
print("Luas permukaan kerucut = ", round(luas,2))
