harga = int(input('masukkan harga:'))
bayar = int(input('masukkan uang:'))
kembalian = bayar-harga

uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

for i in uang :
    pembagian_kembalian = kembalian//i
    kembalian = kembalian % i
    print (f'{int(pembagian_kembalian)} uang Rp{i}')
