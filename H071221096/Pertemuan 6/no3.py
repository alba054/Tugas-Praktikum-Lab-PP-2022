namafile = input(("Masukkan nama file : ")) + ".txt"
asisten = int(input("Masukkan jumlah asisten : "))
filecopy = open(namafile, "w+")

try:
    filecopy.write("+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 10 + "+\n")
    filecopy.write("|" + " Nama" + " " * 17 + "|" + " NIM" + " " * 8 + "|" + " Angkatan" + " " + "|" + "\n")  
    filecopy.write("+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 10 + "+\n") 

    for i in range(asisten):
        nama = input(("Nama : ")).replace(" ", "_")
        if len(nama) > 20:
            print("nama melewati batas inputan")
            raise TypeError()
        
        nim = input(("NIM : "))
        angkatan = input(("Angkatan : "))

        filecopy.write("|" + " " + nama + " " * (22-(len(nama)+1)) + "| " + nim + " " * (12-(len(nim)+1)) + "| " + angkatan + " " * (10-(len(angkatan)+1)) + "|" + "\n")
    filecopy.write("+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 10 + "+\n") 
    print("Berhasil")

except:
    print("Gagal")

filecopy.close()