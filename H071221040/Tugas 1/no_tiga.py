nama = str(input('nama :'))
gaji_pokok = float(input('gaji pokok :'))
total_penjualan = float(input('total penjualan:'))

total_gaji = gaji_pokok + total_penjualan*15/100

print ('total gaji adalah : $', round(total_gaji, 2))