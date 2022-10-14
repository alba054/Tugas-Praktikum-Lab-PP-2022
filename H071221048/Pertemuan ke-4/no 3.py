def myDay(y):
    t=0
    m=0
    d=0
    t=y//365
    m=(y-t*365)//30
    d=y-(t*365+m*30)
    return t,m,d
y=int(input("Masukkan angka:"))  
a=(myDay(y))
print(f"{a[0]} tahun")
print(f"{a[1]} bulan")
print(f"{a[2]} hari")