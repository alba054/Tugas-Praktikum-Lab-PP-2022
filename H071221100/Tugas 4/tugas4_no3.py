def myDay(usia_hari) :
    year= usia_hari//365
    day_remaind= usia_hari%365
    month= day_remaind//30
    days= day_remaind%30
    print(f"{year} tahun")
    print(f"{month} bulan")
    print(f"{days} hari")

hari= int(input("masukkan usia dalam hari"))
myDay(hari)