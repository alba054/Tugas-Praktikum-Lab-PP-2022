golongan = (input("golongan = "))
daya = int(input("daya = "))
pemakaian = int(input("pemakaian = "))

match golongan.upper():

    case "R1" :
        if daya == 900:
            jumlah_tagihan = pemakaian*1352
            print("Jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace(",", ".").replace("/", ","))
        elif daya == 1300 or daya == 2200:
            jumlah_tagihan = pemakaian*1444.70
            print("Jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace(",", ".").replace("/", ","))
        else:
            print("Golongan R1 hanya memiliki daya 900, 1300 dan 2200")

    case "R2":
        if daya >= 3500 and daya <= 5500:
            jumlah_tagihan = pemakaian*1699.53
            print("Jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace(",", ".").replace("/", ","))
        else:
            print("Data tidak valid")
    
    case "R3":
        if daya >= 6600:
            jumlah_tagihan = pemakaian*1699.53
            print("Jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace(",", ".").replace("/", ","))

    case "B2":
        if daya >= 6000 and daya <= 200000:
            jumlah_tagihan = pemakaian*1444.70
            print("Jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace(",", ".").replace("/", ","))
        else:
            print("Data tidak valid")
    
    case "B3":
        if daya > 200000:
            jumlah_tagihan = pemakaian*1114.74
            print("Jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace(",", ".").replace("/", ","))
        else:
            print("Data tidak valid")

    case "I3":
        if daya >= 200000:
            jumlah_tagihan = pemakaian*1314.12
            print("Jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace(",", ".").replace("/", ","))
        else:
            print("Data tidak valid")
    
    case "P1":
        if daya >= 6600 and daya <= 200000:
            jumlah_tagihan = pemakaian*1523.28
            print("Jumlah tagihan anda : Rp{0:,}".format(jumlah_tagihan).replace(".", "/").replace(",", ".").replace("/", ","))
        else:
            print("Data tidak valid")
    
    case _:
        print("Data tidak valid")


    
    



