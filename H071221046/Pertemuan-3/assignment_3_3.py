#Najwa Hanana
#H071221046
#PERTEMUAN 3

print ()
harga = int(input('harga barang: '))
bayar = int(input('nilai uang yang dibayarkan: '))

if harga == bayar:
    print('tidak ada kembalian')
    exit()
if(harga > bayar):
    print("Uang anda tidak cukup")
    exit()
    
kembalian = bayar - harga
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0

if(kembalian >= 100000):
    for a in range(kembalian):
        a += 1
        kembalian -= 100000
        if(kembalian < 100000):
            break
if(kembalian >= 50000):
    for b in range(kembalian):
        b += 1
        kembalian -= 50000
        if(kembalian < 50000):
            break
if(kembalian >= 20000):
    for c in range(kembalian):
        c += 1
        kembalian -= 20000
        if(kembalian < 20000):
            break
if(kembalian >= 10000):
    for d in range(kembalian):
        d += 1
        kembalian -= 10000
        if(kembalian < 10000):
            break
if(kembalian >= 5000):
    for e in range(kembalian):
        e += 1
        kembalian -= 5000
        if(kembalian < 5000):
            break
if(kembalian >= 2000):
    for f in range(kembalian):
        f += 1
        kembalian -= 2000
        if(kembalian < 2000):
            break
if(kembalian >= 1000):
    for g in range(kembalian):
        g += 1
        kembalian -= 1000
        if(kembalian < 1000):
            break

print(a,"uang Rp. 100.000")
print(b,"uang Rp. 50.000")
print(c,"uang Rp. 20.000")
print(d,"uang Rp. 10.000")
print(e,"uang Rp. 5.000")
print(f,"uang Rp. 2.000")
print(g,"uang Rp. 1.000")
print()