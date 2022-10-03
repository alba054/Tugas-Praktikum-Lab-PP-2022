a = int(input("Masukkan nilai total belanja: Rp. "))
b = int(input("Masukkan uang yang dibayar: Rp. "))
c=b-a
d = (100000, 50000, 20000, 10000, 5000,2000, 1000, 500, 200, 100)

jumlah_100000 = 0
jumlah_50000 = 0
jumlah_20000 = 0
jumlah_10000 = 0
jumlah_5000 = 0
jumlah_2000 = 0
jumlah_1000 = 0
jumlah_500 = 0
jumlah_200 = 0
jumlah_100 = 0
 
for i in d:
    if i == 100000:
        jumlah_100000 = c // i
        c = c % i
        print(f"{int(jumlah_100000)}uang Rp{i}")
    elif i == 50000:
        jumlah_50000 = c // i
        c = c % i
        print(f"{int(jumlah_50000)}uang Rp{i}")
    elif i == 20000:
        jumlah_20000 = c // i
        c = c % i
        print(f"{int(jumlah_20000)}uang Rp{i}")
    elif i == 10000:
        jumlah_10000 = c // i
        c = c % i
        print(f"{int(jumlah_10000)}uang Rp{i}")
    elif i == 5000:
        jumlah_5000 = c // i
        c = c % i
        print(f"{int(jumlah_5000)}uang Rp{i}")
    elif i == 2000:
        jumlah_2000 = c // i
        c = c % i
        print(f"{int(jumlah_2000)}uang Rp{i}")
    elif i == 1000:
        jumlah_1000 = c // i
        c = c % i
        print(f"{int(jumlah_1000)}uang Rp{i}")
    elif i == 500:
        jumlah_500 = c // i
        c = c % i
        print(f"{int(jumlah_500)}uang Rp{i}")
    elif i == 200:
        jumlah_200 = c // i
        c = c % i
        print(f"{int(jumlah_200)}uang Rp{i}")
    elif i == 100:
        jumlah = c // i
        c = c % i
        print(f"{int(jumlah_100)}uang Rp{i}")