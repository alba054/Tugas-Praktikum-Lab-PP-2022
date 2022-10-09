a = int(input(""))
def myDay(a):
    tahun = a // 365
    sisa = a % 365
    bulan = sisa // 30
    hari = sisa % 30
    print("%d tahun" % tahun)
    print("%d bulan " % bulan)
    print("%d hari" % hari)
myDay(a)