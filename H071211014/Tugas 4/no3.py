YEAR = 365
MONTH = 30
a = int(input("Masukkan Hari : "))

def myDay(a):
    tahun = 0
    bulan = 0
    while a >= YEAR:
        tahun += 1
        a -= YEAR
    while a >= MONTH:
        bulan += 1
        a -= MONTH
    hari = a%YEAR%MONTH

    return tahun,bulan,hari

x,y,z = myDay(a)
print(x,"tahun")
print(y,"bulan")
print(z,"hari")