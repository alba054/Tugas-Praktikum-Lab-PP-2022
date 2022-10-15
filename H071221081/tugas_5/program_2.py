data = {}
get = ["nama","umur","alamat","daerah asal","sd","smp","sma","hobi"]
def form(lst):
    for i in lst:
        data[i] = input(f"masukkan {i} : ")

def generatePilihan(lst):    
    text = ""
    for i,v in enumerate(lst):
        text += f"{(i+1)}. ubah {v} \n"
    else: 
        text += "9. tampilkan \n"
        text += "0. keluar \n"
    return text
        
def checkPilihan(x):
    if pilih == 0:
        quit()
    elif pilih == 1:
        data["nama"] = input("masukkan nama : ")
    elif pilih == 2:
        data["umur"] = input("masukkan umur : ")
    elif pilih == 3:
        data["alamat"] = input("masukkan alamat : ")
    elif pilih == 3:
        data["daerah asal"] = input("masukkan daerah asal : ")
    elif pilih == 5:
        data["sd"] = input("masukkan sd : ")
    elif pilih == 6:
        data["smp"] = input("masukkan smp : ")
    elif pilih == 7:
        data["sma"] = input("masukkan sma : ")
    elif pilih == 8:
        data["hobi"] = input("masukkan hobi : ")
    elif pilih == 9:
        for k,v in data.items():
            print(f"{k} : {v}")
    else :
        print("tidak ada dalam pilihan")

form(get)
while True:
    print(generatePilihan(get))
    print()
    pilih = int(input("pilih : "))
    print()
    checkPilihan(pilih)
    
    print()
