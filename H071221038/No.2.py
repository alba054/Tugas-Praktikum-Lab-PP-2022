detik = int(input("Masukkan detik = "))

jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

result = str(jam)+":"+str(menit)+":"+str(detik)
print(result)
