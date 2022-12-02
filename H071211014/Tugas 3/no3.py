harga_barang = int(input("Harga Barang : "))
uang_yg_dibayarkan = int(input("Nominal Uang : "))

kembalian = uang_yg_dibayarkan-harga_barang
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0

if harga_barang < uang_yg_dibayarkan:
    while kembalian >= 100000:
        x1 += 1
        kembalian -= 100000

    while kembalian >= 50000:
        x2 += 1
        kembalian -= 50000

    while kembalian >= 20000:
        x3 += 1
        kembalian -= 20000

    while kembalian >= 10000:
        x4 += 1
        kembalian -= 10000

    while kembalian >= 5000:
        x5 += 1
        kembalian -= 5000

    while kembalian >= 2000:
        x6 += 1
        kembalian -= 2000

    while kembalian >= 1000:
        x7 += 1
        kembalian -= 1000
else:
    print("Inputan Tidak Valid")

print(x1, "uang Rp. 100.000" )
print(x2, "uang Rp. 50.000" )
print(x3, "uang Rp. 20.000" )
print(x4, "uang Rp. 10.000" )
print(x5, "uang Rp. 5.000" )
print(x7, "uang Rp. 2.000" )
print(x7, "uang Rp. 1.000" )