#Najwa Hanana
#H071221046
# Konversi detik ke jam:menit:detik berdasarkan detik

print ("Konversi Detik")
print ("--------------")

detik = int(input("Masukkan jumlah detik yang ingin diconvert : "))

jam = detik//3600
sisa = detik%3600
menit = sisa//60
detik = sisa%60

print ("Hasil convert adalah : ",jam,':',menit,':',detik)
print ("Hasil convert adalah : ",jam,"Jam ",menit,"Menit ",detik,"Detik")