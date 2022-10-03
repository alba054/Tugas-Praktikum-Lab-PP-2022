total_detik = int(input('masukkan detik :'))

jam = total_detik//3600
sisa_detik = total_detik%3600
menit = sisa_detik//60
detik = sisa_detik%60

print (str(jam)+":"+str(menit)+":"+str(detik))