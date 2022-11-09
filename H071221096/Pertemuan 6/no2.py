fileoriginal = input("Masukkan nama file: ")
filecopy = input("Masukkan nama file baru: ")

try:
    with open(f"{fileoriginal}.txt" , 'r') as file:
        a = file.read()
except:
    print("Gagal")
else:
    with open(f"{fileoriginal}.txt") as line:
        spasi = line.readlines()
    with open(f"{filecopy}.txt" , 'w') as index:
        for i in spasi:
            index.write(i.rjust(25))
    print("Berhasil")