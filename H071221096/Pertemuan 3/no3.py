x = int(input("harga barang : "))
y = int(input("pembayaran : "))
kembalian = y - x
pecahan = (100000, 50000, 20000, 10000, 5000, 2000, 1000)

if y >= x:
    for uang in pecahan:
        banyak = kembalian // uang
        kembalian = kembalian - banyak * uang
        print(banyak , "uang Rp. " , uang)
else:
    print("Inputan tidak valid")
    
    

    



