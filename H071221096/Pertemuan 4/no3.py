x = int(input("Masukkan Usia dalam hari : "))

def myDay(x):
    
    tahun = x // 365
    sisa = x % 365

    bulan = sisa // 30
    sisa_hari = sisa % 30

    hari = sisa_hari

    print(tahun , "tahun")
    print(bulan , "bulan")
    print(hari , "hari")

myDay(x)